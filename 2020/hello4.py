#!/usr/bin/env python3
# Purpose: Say hello

import sys, os, argparse

def greet(name: str) -> str:
    return f'Hello, {name}!'


def test_greet() -> None:
    assert greet('World') == 'Hello, World!'
    assert greet('Terra Firme') == 'Hello, Terra Firme!'


def main() -> None:
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('name', help='The name to greet')
    args = parser.parse_args()
    print(greet(args.name))


if __name__ == '__main__':
    main()
