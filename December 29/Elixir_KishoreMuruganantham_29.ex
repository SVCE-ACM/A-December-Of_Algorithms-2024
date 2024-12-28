defmodule PathFinder do
  def minimum_weight_path(n, m, portals) do
    graph = build_graph(n, m, portals)

    pq = [{0, {1, 1}}]
    distances = initialize_distances(n, m)

    distances = Map.put(distances, {1, 1}, 0)

    while pq != [] do
      {current_dist, current_node} = Enum.min_by(pq, fn {dist, _node} -> dist end)
      pq = List.delete(pq, {current_dist, current_node})

      if current_node == {n, m} do
        return current_dist
      end

      if current_dist > Map.get(distances, current_node) do
        continue
      end

      neighbors = Map.get(graph, current_node, [])
      
      pq = Enum.reduce(neighbors, pq, fn {neighbor, weight}, acc ->
        distance = current_dist + weight
        if distance < Map.get(distances, neighbor, :infinity) do
          new_distances = Map.put(distances, neighbor, distance)
          [{distance, neighbor} | acc]
        else
          acc
        end
      end)
    end

    -1
  end

  defp build_graph(n, m, portals) do
    graph = for i <- 1..n, j <- 1..m, into: %{}, do: {{i, j}, []}

    graph = Enum.reduce(portals, graph, fn {x1, y1, x2, y2, w}, acc ->
      acc
      |> Map.update({x1, y1}, [{ {x2, y2}, w }], &([{ {x2, y2}, w } | &1]))
      |> Map.update({x2, y2}, [{ {x1, y1}, w }], &([{ {x1, y1}, w } | &1]))
    end)

    directions = [{0, 1}, {1, 0}, {0, -1}, {-1, 0}]
    Enum.reduce(1..n, graph, fn i, acc ->
      Enum.reduce(1..m, acc, fn j, acc2 ->
        Enum.reduce(directions, acc2, fn {di, dj}, acc3 ->
          ni = i + di
          nj = j + dj
          if ni >= 1 and ni <= n and nj >= 1 and nj <= m do
            Map.update(acc3, {i, j}, [{ {ni, nj}, 0 }], &([{ {ni, nj}, 0 } | &1]))
          else
            acc3
          end
        end)
      end)
    end)
  end

  defp initialize_distances(n, m) do
    for i <- 1..n, j <- 1..m, into: %{}, do: {{i, j}, :infinity}
  end
end

# Example usage:
portals = [{1, 1, 2, 1, 1}, {2, 1, 3, 1, 1}, {3, 1, 3, 2, 1}, {3, 2, 3, 3, 1}, {3, 3, 2, 3, 1}, {2, 3, 1, 3, 1}]
IO.puts(PathFinder.minimum_weight_path(3, 3, portals)) # Output will be the minimum path weight
