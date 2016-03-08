#!/usr/bin/python
# -*- coding: UTF-8 -*-
import thread
import totalOperation

# thread.start_new_thread( totalOperation.writeToFile, (0,10) )
# thread.start_new_thread( totalOperation.writeToFile, (10,10) )

totalOperation.writeToFile(0,1000)
