function count_robot_paths(steps, distance)
    if distance == 0
        return 1
    end

    dp = zeros(Int, distance + 1)
    dp[1] = 1

    for i in 2:distance + 1
        for step in steps
            if i - step >= 1
                dp[i] += dp[i - step]
            end
        end
    end

    return dp[distance + 1]
end
