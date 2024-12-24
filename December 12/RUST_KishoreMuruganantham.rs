use std::collections::{VecDeque, HashMap};
use std::time::Duration;
use std::thread;

#[derive(Debug)]
struct SmartTicketingSystem {
    queue: VecDeque<(String, i32)>,
    results: Vec<String>,
    total_tickets: i32,
    available_tickets: i32,
    vip_bonus: i32,
    ticket_history: Vec<String>,
    error_log: Vec<String>,
    special_offer: Option<SpecialOffer>,
    logs_enabled: bool,
}

#[derive(Debug)]
struct SpecialOffer {
    name: String,
    percentage: i32,
}

impl SmartTicketingSystem {
    fn new(total_tickets: i32, vip_bonus: i32) -> Self {
        SmartTicketingSystem {
            queue: VecDeque::new(),
            results: Vec::new(),
            total_tickets,
            available_tickets: total_tickets,
            vip_bonus,
            ticket_history: Vec::new(),
            error_log: Vec::new(),
            special_offer: None,
            logs_enabled: true,
        }
    }

    fn log_event(&mut self, event: String) {
        if self.logs_enabled {
            println!("[LOG] {}", event);
        }
        self.ticket_history.push(event);
    }

    fn set_special_offer(&mut self, offer_name: &str, offer_percentage: i32) {
        self.special_offer = Some(SpecialOffer {
            name: offer_name.to_string(),
            percentage: offer_percentage,
        });
        self.log_event(format!(
            "Special offer {} set with {}% discount.",
            offer_name, offer_percentage
        ));
    }

    fn reset_special_offer(&mut self) {
        self.special_offer = None;
        self.log_event("Special offer has been reset.".to_string());
    }

    fn process_request(&mut self, request: &str) {
        let parts: Vec<&str> = request.split_whitespace().collect();
        if parts.len() < 2 {
            let error_message = format!("Error processing request '{}': Invalid request", request);
            self.error_log.push(error_message.clone());
            self.log_event(error_message);
            return;
        }

        let customer = parts[0].to_string();
        let num_tickets: i32 = match parts[1].parse() {
            Ok(val) => val,
            Err(_) => {
                let error_message = format!("Error processing request '{}': Invalid number of tickets", request);
                self.error_log.push(error_message.clone());
                self.log_event(error_message);
                return;
            }
        };

        let is_vip = parts.len() > 2 && parts[2] == "VIP";

        if is_vip {
            self.queue.push_front((customer, num_tickets));
            self.log_event(format!(
                "VIP customer {} added to the queue with {} tickets.",
                customer, num_tickets
            ));
        } else {
            self.queue.push_back((customer, num_tickets));
            self.log_event(format!(
                "Regular customer {} added to the queue with {} tickets.",
                customer, num_tickets
            ));
        }
    }

    fn apply_special_offer(&self, num_tickets: i32) -> i32 {
        if let Some(offer) = &self.special_offer {
            let discount = num_tickets * offer.percentage / 100;
            let discounted_tickets = num_tickets - discount;
            self.log_event(format!(
                "Special offer applied. Discounted tickets from {} to {}.",
                num_tickets, discounted_tickets
            ));
            return discounted_tickets;
        }
        num_tickets
    }

    fn allocate_tickets(&mut self) {
        while let Some((customer, num_tickets)) = self.queue.pop_front() {
            if self.available_tickets == 0 {
                self.results.push(format!("{} was not served", customer));
                continue;
            }

            let num_tickets = self.apply_special_offer(num_tickets);
            let tickets_allocated = self.available_tickets.min(num_tickets);
            self.available_tickets -= tickets_allocated;

            if tickets_allocated > 0 {
                self.results.push(format!("{} purchased {} tickets", customer, tickets_allocated));
                self.log_event(format!(
                    "Allocated {} tickets to {}.",
                    tickets_allocated, customer
                ));
            } else {
                self.results.push(format!("{} was not served", customer));
                self.log_event(format!("Could not allocate tickets to {}.", customer));
            }
        }
    }

    fn handle_multiple_requests(&mut self, requests: Vec<&str>) {
        for request in requests {
            self.process_request(request);
        }

        self.allocate_tickets();
    }

    fn show_results(&self) {
        println!("Ticketing Results:");
        for result in &self.results {
            println!("{}", result);
        }
    }

    fn show_ticket_history(&self) {
        println!("Ticketing History:");
        for event in &self.ticket_history {
            println!("{}", event);
        }
    }

    fn show_error_log(&self) {
        if !self.error_log.is_empty() {
            println!("Error Log:");
            for error in &self.error_log {
                println!("{}", error);
            }
        } else {
            println!("No errors found.");
        }
    }
}

fn main() {
    let mut ticket_system = SmartTicketingSystem::new(10, 2);
    ticket_system.set_special_offer("HolidaySale", 10);

    let requests = vec![
        "Alice 3 VIP",
        "Bob 5",
        "Charlie 2",
        "David 1 VIP",
        "Eve 4",
        "Frank 6 VIP",
        "Grace 2",
        "Hannah 2",
        "Ivy 3",
        "Jack 1 VIP",
    ];

    ticket_system.handle_multiple_requests(requests);
    ticket_system.show_results();

    ticket_system.show_ticket_history();
    ticket_system.show_error_log();

    thread::sleep(Duration::from_secs(2));
    ticket_system.reset_special_offer();

    let new_requests = vec![
        "Kim 2",
        "Liam 5 VIP",
        "Mona 3",
        "Nina 1 VIP",
    ];
    ticket_system.handle_multiple_requests(new_requests);
    ticket_system.show_results();
}
