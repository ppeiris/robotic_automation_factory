# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Package sorting function for a robotic automation factory. Classifies packages as STANDARD, SPECIAL, or REJECTED based on dimensions and mass.

## Commands

- **Run tests**: `pytest test_sort.py -v`
- **Run single test**: `pytest test_sort.py::test_name -v`

## Requirements

- All solutions must be implemented in Python.
- Use pytest to test the function, ensuring all edge cases are covered (zero/negative dimensions, boundary values, float inputs, etc.).

## Architecture

- `sort.py` — Single function `sort(width, height, length, mass)` that returns a stack name string
- `test_sort.py` — pytest test suite covering standard, special, rejected, and edge cases
