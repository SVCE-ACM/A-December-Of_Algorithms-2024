function result = robot_return_to_origin(moves)
    x = 0;
    y = 0;
    
    for i = 1:length(moves)
        move = moves(i);
        
        if move == 'R'
            x = x + 1;
        elseif move == 'L'
            x = x - 1;
        elseif move == 'U'
            y = y + 1;
        elseif move == 'D'
            y = y - 1;
        end
    end
    
    result = (x == 0) && (y == 0);
end
