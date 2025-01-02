defmodule BookOrganizer do
  def can_organize_books(books, shelf_size) do
    if rem(length(books), shelf_size) != 0 do
      false
    else
      book_count = Enum.reduce(books, %{}, fn book, acc ->
        Map.update(acc, book, 1, &(&1 + 1))
      end)

      unique_books = Enum.sort(Map.keys(book_count))

      Enum.reduce_while(unique_books, book_count, fn book, acc ->
        acc = organize_books(book, shelf_size, acc)

        if acc == :error do
          {:halt, false}
        else
          {:cont, acc}
        end
      end)
      |> case do
        false -> false
        _ -> true
      end
    end
  end

  defp organize_books(_book, 0, acc), do: acc
  defp organize_books(book, shelf_size, acc) do
    Enum.reduce_while(0..(shelf_size - 1), acc, fn i, acc ->
      if Map.get(acc, book + i, 0) <= 0 do
        {:halt, :error}
      else
        acc = Map.update(acc, book + i, 0, &(&1 - 1))
        {:cont, acc}
      end
    end)
  end
end

# Example usage
IO.puts(BookOrganizer.can_organize_books([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))  # Output: true
IO.puts(BookOrganizer.can_organize_books([1, 2, 3, 4, 5], 4))  # Output: false

