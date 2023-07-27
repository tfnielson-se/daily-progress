defmodule Fizzbuzz do

  def say_hi() do
    IO.inspect("Hello, welcome to Fizzbuzz")
  end

  def play_game(filename) do
    say_hi()

    filename
    |> File.read()
    |> get_numbers()
    |> string_to_int()
    |> fizz_buzz_it()
  end

  def get_numbers({:ok, numbers}), do: numbers |> String.split(",")
  def get_numbers({:error, e_reason}), do: e_reason |> IO.inspect()

  def string_to_int(num_list_string) do
    num_list_string
    |> Enum.map(&String.to_integer/1)
  end

  def fizz_buzz_it(list_of_nums) do
    list_of_nums |> Enum.map(fn num -> fizz_or_buzz(num) end)
  end

  def fizz_or_buzz(num) when rem(num, 3) == 0, do: :fizz
  def fizz_or_buzz(num) when rem(num, 5) == 0, do: :buzz
  def fizz_or_buzz(num), do: num

end
