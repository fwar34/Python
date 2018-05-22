#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
# File Name: dbus.py
# Created Time: Wed 22 Mar 2017 03:14:50 PM CST
# Author: Feng
# Content: python调用dbus

import dbus
# import dbus.decorators
# import dbus.glib
import gobject

# bus = dbus.SystemBus()
bus = dbus.SessionBus()
bus_obj = bus.get_object('org.freedesktop.DBus', '/')
iface = dbus.Interface(bus_obj, 'org.desktop.DBus')
names = iface.ListActivatableNames()
for n in names:
    print n
