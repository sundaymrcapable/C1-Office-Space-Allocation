#!/usr/bin/env python
# encoding: utf-8

'''

This is the parent class for subclasses: LivingSpace and Office
The subclasses will inherit the available methods

'''


class Room:
    def __init__(self, room_name, room_type):
        self.room_type = room_type
        self.room_name = room_name

    # Noticed this function could be useful elsewhere apart from getting the
    # capacity.
    def room_details(self):
        self.room_capacity = 0
        if self.room_type.upper() != 'OFFICE':
            self.room_capacity = 4
        else:
            self.room_capacity = 6
        return self.room_type, self.room_name, self.room_capacity
