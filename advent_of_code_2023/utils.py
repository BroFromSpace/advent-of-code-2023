from functools import wraps
from pathlib import Path
from time import perf_counter
from typing import Callable, ParamSpec, TypeVar

from rich.box import ROUNDED
from rich.table import Table

from advent_of_code_2023.console import console

T = TypeVar("T")
P = ParamSpec("P")


def get_input_as_lines(input_path: Path, encoding: str = "utf-8") -> list[str]:
	with open(input_path, "r", encoding=encoding) as f:
		return f.readlines()


def get_input_as_content(input_path: Path, encoding: str = "utf-8") -> str:
	with open(input_path, "r", encoding=encoding) as f:
		return f.read()


def pretty_output(
	title: str, caption: str
) -> Callable[[Callable[P, T]], Callable[P, T]]:
	def decorator(func: Callable[P, T]) -> Callable[P, T]:
		@wraps(func)
		def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
			start_time = perf_counter()
			result = func(*args, **kwargs)
			elapsed_time = perf_counter() - start_time

			table = Table(title=title, caption=caption, box=ROUNDED, safe_box=True)
			table.add_column(
				"Answer", style="cyan", justify="center", vertical="middle"
			)
			table.add_column(
				"Time", style="magenta", justify="center", vertical="middle"
			)
			table.add_row(f"{result}", f"{elapsed_time:.6f} seconds")

			console.print(table, new_line_start=True)

			return result

		return wrapper

	return decorator
