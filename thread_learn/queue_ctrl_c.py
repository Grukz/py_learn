#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import Queue
import threading

import requests
from invoke import task

from models import (
    mysqldb,
    Bar,
)

lock = threading.Lock()
worker_number = 80
tasks = range(1200)
url = 'http://www.baidu.com/'


def do_work(item):
    text = requests.get(url).text
    print(item, len(text))


def worker(q):
    while Queue.running:
        try:
            item = q.get(timeout=0.1)
            do_work(item)
        except Queue.Empty as e:
            print(type(e), str(e))
        if q.empty():
            Queue.running = False


@task
def main_of_func():
    Queue.running = True
    q = Queue.Queue()
    [q.put(item) for item in tasks]
    [threading.Thread(target=worker, args=(q, )).start() for i in range(worker_number)]
    try:
        while Queue.running:
            time.sleep(1)
    except KeyboardInterrupt:
        Queue.running = False


class Printer(threading.Thread):
    running = True

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while Printer.running:
            if self.queue.empty():
                # time.sleep(1)
                Printer.running = False
                print(self, 'quit')
                break
            try:
                item = self.queue.get(block=False)
                text = requests.get(url).text
                length = len(text)
                bars = [bar.length for bar in Bar.filter(Bar.id < 10000)]
                self.work(length)
            except Queue.Empty as e:
                print(type(e), str(e))
        else:
            print(self, 'quit')

    @mysqldb.atomic()
    def work(self, length):
        bar = Bar.create(length=length)
        print(bar, bar.length, bar.id)


@task
def main_of_class():
    q = Queue.Queue(len(tasks) + 1)
    bars = [bar.length for bar in Bar.filter(Bar.id < 10000)]
    [q.put(item) for item in tasks]
    threads = [Printer(q) for i in range(worker_number)]
    [t.start() for t in threads]
    try:
        while Printer.running:
            time.sleep(1)
    except KeyboardInterrupt:
        Printer.running = False
    time.sleep(9)
    for t in threads:
        # continue
        if t.is_alive():
            t.join()
    print('Over..............................................................')


class Useless(threading.Thread):
    running = True

    def __init__(self, data):
        threading.Thread.__init__(self)
        self.data = data

    def run(self):
        while Useless.running:  # self.running, problematic
            lock.acquire()
            if len(self.data) == 0:
                Useless.running = False  # self.running, problematic
                item = None
            else:
                item = self.data.pop(0)
            lock.release()
            if item is not None:
                text = requests.get(url).text
                print(item, len(text))


@task
def main_of_useless():
    data = list(tasks)
    [Useless(data).start() for i in range(worker_number)]
    try:
        while Useless.running:
            time.sleep(1)
    except KeyboardInterrupt:
        Useless.running = False

if __name__ == '__main__':
    main_of_class()
