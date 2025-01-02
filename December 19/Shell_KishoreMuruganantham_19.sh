#!/bin/bash

tower_of_hanoi() {
    local n=$1
    local source=$2
    local destination=$3
    local auxiliary=$4

    if [ $n -eq 0 ]; then
        return
    fi

    tower_of_hanoi $((n - 1)) $source $auxiliary $destination
    echo "Move disk $n from $source to $destination"
    tower_of_hanoi $((n - 1)) $auxiliary $destination $source
}

num_disks=4
start="A"
destination="C"
auxiliary="B"

echo "Minimum number of moves: $(( 2 ** num_disks - 1 ))"
echo "Sequence of moves:"

tower_of_hanoi $num_disks $start $destination $auxiliary
