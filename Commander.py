#!/usr/bin/env python

# Main logic file for Commander.

from DBManager import DBManager
import argparse
import os

def copy_to_clipboard(data):
        os.system("echo '%s\c' | pbcopy" % data)

def main():
    parser = argparse.ArgumentParser(description='Process arguments for Commander')
    parser.add_argument('-a', '--add', nargs='*', help="Add a command to the database")
    parser.add_argument('-d', '--delete', help="Delete a command from the database.", type=int)
    parser.add_argument('-s', '--search', help="Search for a command based on ID.")
    parser.add_argument('-u', '--update', nargs='*', help="Update a command in the database.")
    args = parser.parse_args()

    connector = DBManager('commands')

    if args.search:
        if args.search == "all":
            for i in connector.show_all_records():
                print("Number: " + str(i[0]) + "\nTitle: " + i[1] + "\nCommand: " + i[2])
        else:
            command_to_copy = connector.show_record_by_id(args.search)[2]
            copy_to_clipboard(command_to_copy)
            print connector.show_record_by_id(args.search)

    elif args.delete:
        connector.del_record_by_id(args.delete)
    elif args.add:
        connector.add_record(args.add)
    elif args.update:
        connector.update_record(args.update)
    else:
        parser.print_help()

main()


