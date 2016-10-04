#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module that returns today's date"""

import datetime

CURDATE = None


def get_current_date():
    """Provides user current date.

    Args:
        No parameters to be entered.

    Returns:
        Today's date.

    Examples:

        >>> print task_01.CURDATE
            None
        >>>task_01.get_current_date()
            datetime.date(2016, 10, 4)
        Command Line, CURDATE has the date value:
        >>>>>> CURDATE
            datetime.date(2016, 10, 4)
    """
    date = datetime.date.today()
    return date


if __name__ == '__main__':
    CURDATE = get_current_date()
