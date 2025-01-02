package main

import (
	"fmt"
	"os"
	"encoding/gob"
	"container/heap"
)

type Task struct {
	Description string
	Priority    int
}

type TaskScheduler struct {
	Heap      *TaskHeap
	TaskMap   map[string]*Task
	Filename  string
}

func NewTaskScheduler(filename string) *TaskScheduler {
	scheduler := &TaskScheduler{
		Heap:     &TaskHeap{},
		TaskMap:  make(map[string]*Task),
		Filename: filename,
	}
	scheduler.LoadTasks()
	return scheduler
}

func (s *TaskScheduler) AddTask(description string, priority int) {
	if _, exists := s.TaskMap[description]; exists {
		fmt.Printf("Task '%s' already exists.\n", description)
		return
	}
	task := &Task{Description: description, Priority: priority}
	heap.Push(s.Heap, task)
	s.TaskMap[description] = task
	s.SaveTasks()
}

func (s *TaskScheduler) RemoveTask(description string) {
	if task, exists := s.TaskMap[description]; exists {
		// Remove task from heap
		heap.Remove(s.Heap, task.Index)
		delete(s.TaskMap, description)
		s.SaveTasks()
	} else {
		fmt.Printf("Task '%s' not found.\n", description)
	}
}

func (s *TaskScheduler) SearchTask(description string) *Task {
	return s.TaskMap[description]
}

func (s *TaskScheduler) DisplayTasks() []Task {
	var tasks []Task
	for _, task := range *s.Heap {
		tasks = append(tasks, *task)
	}
	return tasks
}

func (s *TaskScheduler) SaveTasks() {
	file, err := os.Create(s.Filename)
	if err != nil {
		fmt.Println("Error creating file:", err)
		return
	}
	defer file.Close()

	encoder := gob.NewEncoder(file)
	err = encoder.Encode(s.Heap)
	if err != nil {
		fmt.Println("Error saving tasks:", err)
	}
}

func (s *TaskScheduler) LoadTasks() {
	if _, err := os.Stat(s.Filename); err == nil {
		file, err := os.Open(s.Filename)
		if err != nil {
			fmt.Println("Error opening file:", err)
			return
		}
		defer file.Close()

		decoder := gob.NewDecoder(file)
		err = decoder.Decode(s.Heap)
		if err != nil {
			fmt.Println("Error loading tasks:", err)
			return
		}
	}
}

type TaskHeap []*Task

func (h TaskHeap) Len() int { return len(h) }
func (h TaskHeap) Less(i, j int) bool {
	return h[i].Priority > h[j].Priority
}
func (h TaskHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
	h[i].Index = i
	h[j].Index = j
}

func (h *TaskHeap) Push(x interface{}) {
	n := len(*h)
	task := x.(*Task)
	task.Index = n
	*h = append(*h, task)
}

func (h *TaskHeap) Pop() interface{} {
	old := *h
	n := len(old)
	task := old[n-1]
	task.Index = -1
	*h = old[0 : n-1]
	return task
}

func main() {
	scheduler := NewTaskScheduler("tasks.gob")
	scheduler.AddTask("Complete Assignment", 2)
	scheduler.AddTask("Buy Groceries", 1)
	fmt.Println("Tasks:", scheduler.DisplayTasks())
	scheduler.RemoveTask("Complete Assignment")
	fmt.Println("Tasks after removal:", scheduler.DisplayTasks())
}
