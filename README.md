# Student_Survival_Manager

**Description**

Student Survival Manager is a small Python application designed to help students manage their university tasks, deadlines and workload.
Instead of only showing a normal to-do list, the application calculates **Panic Points** based on how close a deadline is and how difficult the task is. This gives students a simple and funny way to see which tasks need their attention first. 

**Problem** 

A student struggles to organize the multiple tasks assigned and fails exams :)

**Scenario**

Student Survival Manager manages students' workload by tracking tasks, checking deadlines and using **Panic Points** to see which tasks are the most urgent

### 👤 User Roles

| Role | Description |
|------|-------------|
| **Student** | Creates and prioritizes tasks|

#### US-01: Add tasks

**As an** student, **I want** to add a task with a description, **so that** I can keep track of my university work 

**Acceptance criteria**
- The application reads `menu.txt` at startup.
- Each line has the format `Name;Size;Price` (three fields separated by `;`), e.g., `Margherita;Medium;12.50`.
- *Given* the owner adds the line `Quattro Formaggi;Large;18.00` to `menu.txt`, *when* the application is restarted and the menu is displayed, *then* `6. Quattro Formaggi (Large) - CHF 18.00` appears as the last line of the menu.
- *Given* `menu.txt` contains the line `Calzone;Large;abc`, *when* the menu is loaded, *then* the warning `⚠️ Skipping invalid line: Calzone;Large;abc` is displayed, the line is not added to the menu, and all valid lines are still loaded.
- *Given* a line in `menu.txt` does not contain exactly three fields (e.g., `Marinara;Small`), *when* the menu is loaded, *then* that line is not added to the menu and the application does not crash.
- *Given* `menu.txt` does not exist, *when* the application starts, *then* a new `menu.txt` is created containing the three starter pizzas Margherita (Medium, 12.50), Salami (Large, 15.00), and Funghi (Small, 9.00), and these three pizzas are displayed in the menu.

  
#### US-02: Show the prioritized tasks

**As a** student, **I want** prioritize my tasks, **so that** I can see them organized.

**Acceptance criteria**
- The menu is displayed when the staff member selects option `1` ("Show menu") in the main menu.
- The menu is also displayed automatically before a new order is started (option `2`).
- Each pizza is shown on its own line in the format `<No>. <Name> (<Size>) - CHF <Price>`, e.g., `1. Margherita (Medium) - CHF 12.50`.
- The numbering starts at `1` and follows the order of the lines in `menu.txt`.
- All prices are displayed with exactly two decimal places.
- *Given* `menu.txt` contains the five pizzas listed above, *when* the menu is displayed, *then* exactly five numbered lines are shown, from `1. Margherita (Medium) - CHF 12.50` to `5. Diavola (Large) - CHF 17.50`.

---

#### US-03: Calculate panic points

**As a** student, **I want** the application to calculate panic points, **so that** I know how urgent my tasks are.

**Acceptance criteria**
- The staff member selects a pizza by entering its menu number.
- After selecting a pizza, the staff member enters a quantity (a whole number).
- Each selected pizza has a unit price taken from the menu.
- The system multiplies the unit price by the quantity to calculate the item total.
- The item total is displayed with two decimal places, e.g., `2x Margherita (Medium) - CHF 25.00`.
- *Given* a pizza with a unit price of CHF 12.50 and a quantity of 2, *when* the item total is calculated, *then* the result is CHF 25.00.
- *Given* a pizza with a unit price of CHF 17.50 and a quantity of 3, *when* the item total is calculated, *then* the result is CHF 52.50.
- *Given* a quantity of 0 or smaller (e.g., `0` or `-2`), *when* the item total is calculated, *then* the result is always CHF 0.00 (the calculation never returns a negative amount).
- Entering `done` instead of a pizza number finishes the order.

---

#### US-04: See current panic level

**As a** student, **I want** to see my "panic level", **so that** I can quickly understand my current workload

**Acceptance criteria**
- *Given* the menu has five pizzas, *when* the staff member enters `0`, `6`, `-1`, `abc`, or an empty input as pizza number, *then* the message `⚠️ Invalid choice.` is displayed, nothing is added to the order, and the staff member is asked for a pizza number again.
- *Given* a valid pizza was selected, *when* the staff member enters `0`, a negative number, a decimal number (e.g., `1.5`), or text (e.g., `two`) as quantity, *then* the message `⚠️ Invalid quantity.` is displayed, the pizza is not added to the order, and the staff member is asked for the quantity again.
- *Given* the main menu is displayed, *when* the staff member enters anything other than `1`, `2`, or `3`, *then* the message `⚠️ Invalid choice.` is displayed and the main menu is shown again.
- Input is accepted regardless of surrounding spaces and upper/lower case for the keyword, e.g., ` DONE ` finishes the order just like `done`.
- In none of the cases above does the program terminate with an error (no Python traceback is shown).

---

#### US-05: View task deadline 

**As a** student, **I want** to see the task deadline, **so that** I can check how much time I have left.

**Acceptance criteria**
- After each successfully added item, the message `Added! Current subtotal: CHF <amount>` is displayed.
- The subtotal is the sum of all item totals (unit price × quantity) in the current order, before any discount.
- The subtotal is displayed with two decimal places.
- *Given* the order already contains 1x Salami (CHF 15.00), *when* 2x Margherita (CHF 12.50 each) are added, *then* the message `Added! Current subtotal: CHF 40.00` is displayed.
- An invalid input (see US-04) does not change the subtotal.

---

#### US-06: View task description 

**As a** student, **I want** to see the task description, **so that** I can check what the task is about.

**Acceptance criteria**
- After each successfully added item, the message `Added! Current subtotal: CHF <amount>` is displayed.
- The subtotal is the sum of all item totals (unit price × quantity) in the current order, before any discount.
- The subtotal is displayed with two decimal places.
- *Given* the order already contains 1x Salami (CHF 15.00), *when* 2x Margherita (CHF 12.50 each) are added, *then* the message `Added! Current subtotal: CHF 40.00` is displayed.
- An invalid input (see US-04) does not change the subtotal.

---

#### US-07: View difficulty level of the task

**As a** student, **I want** to see the task difficuty level, **so that** I can check the effort that I have to put into it.

**Acceptance criteria**
- After each successfully added item, the message `Added! Current subtotal: CHF <amount>` is displayed.
- The subtotal is the sum of all item totals (unit price × quantity) in the current order, before any discount.
- The subtotal is displayed with two decimal places.
- *Given* the order already contains 1x Salami (CHF 15.00), *when* 2x Margherita (CHF 12.50 each) are added, *then* the message `Added! Current subtotal: CHF 40.00` is displayed.
- An invalid input (see US-04) does not change the subtotal.

---

#### US-08: Mark as a completed

**As a** student, **I want** to mark the task as completed, **so that** I can keep track on my progress.

**Acceptance criteria**
- **Rule 1 – Free pizza:** If an order contains **more than 3** pizzas in total (sum of all quantities), the cheapest pizza (one piece) is free.
- **Rule 2 – 10 % discount:** If the amount after Rule 1 is **CHF 50.00 or more**, a discount of 10 % is deducted from that amount.
- Rule 1 is always applied before Rule 2.
- Each applied discount is listed with its name and amount, e.g., `Free pizza: Funghi (-CHF 9.00)` or `10% discount (-CHF 5.25)`.
- The final total is displayed with two decimal places.

| Given this order | Subtotal | Discount(s) applied | Then the total is |
|------------------|---------:|---------------------|------------------:|
| 2x Margherita | 25.00 | none | **CHF 25.00** |
| 1x Margherita, 1x Salami, 1x Funghi, 1x Hawaii (4 pizzas) | 50.50 | Free pizza: Funghi (-9.00) → 41.50 is below 50.00, so no 10 % | **CHF 41.50** |
| 3x Diavola (3 pizzas) | 52.50 | 10% discount (-5.25) | **CHF 47.25** |
| 1x Salami, 2x Diavola (exactly CHF 50.00) | 50.00 | 10% discount (-5.00) | **CHF 45.00** |
| 2x Diavola, 1x Hawaii (CHF 49.00) | 49.00 | none | **CHF 49.00** |
| 4x Diavola, 1x Funghi (5 pizzas) | 79.00 | Free pizza: Funghi (-9.00) → 70.00; 10% discount (-7.00) | **CHF 63.00** |

---

#### US-09: Save tasks to a file

**As a** student, **I want** my tasks to be saved, **so that** I do not lose them.

**Acceptance criteria**
- The summary is shown after the staff member enters `done`.
- The summary starts with the heading `--- ORDER SUMMARY ---`.
- It lists every ordered item with quantity, name, size, and item total, e.g., `2x Margherita (Medium) - CHF 25.00`.
- It lists every applied discount (see US-06).
- It ends with the final amount in the format `TOTAL: CHF <amount>` with two decimal places.
- *Given* the staff member enters `done` without having added any pizza, *when* the order is finished, *then* the message `⚠️ No pizzas selected.` is displayed, no summary and no invoice are created, and the main menu is shown again.

---

#### US-10: View the dashboard

**As a** student, **I want** to see a summary of my current workload, **so that** I can understand my situation immediately.

**Acceptance criteria**
- An invoice file is created automatically for every order that contains at least one pizza.
- The file name follows the pattern `invoice_<NNN>.txt` with a three-digit number, e.g., `invoice_001.txt`.
- *Given* no invoice file exists yet, *when* an order is completed, *then* the file `invoice_001.txt` is created.
- *Given* `invoice_001.txt` and `invoice_002.txt` already exist, *when* an order is completed, *then* the file `invoice_003.txt` is created and the existing files remain unchanged.
- The invoice contains the heading `🍕 PIZZA RP INVOICE`, one line per ordered item (quantity, name, size, item total), all applied discounts, and the line `TOTAL: CHF <amount>`.
- The amounts in the invoice file are identical to the amounts shown in the order summary (US-07).
- After saving, the message `✅ Invoice saved as invoice_<NNN>.txt` is displayed.

---

#### US-11: Edit a task 

**As a** student, **I want** to edit the task, **so that** I can correct or update its informations.

**Acceptance criteria**
- *Given* the main menu is displayed, *when* the staff member enters `3`, *then* the message `Goodbye 👋` is displayed and the program ends.
- All invoices created during the session remain saved after the program has ended.

---

#### US-12: Exit the application

**As a** student, **I want** to close the application via the main menu, **so that** I can finish using the program safely.

**Acceptance criteria**
- *Given* the main menu is displayed, *when* the staff member enters `3`, *then* the message `Goodbye 👋` is displayed and the program ends.
- All invoices created during the session remain saved after the program has ended.

---




**Use cases:**
- Show Menu (from `menu.txt`)
- Create Order (choose pizzas)
- Show Current Order and Total
- Print Invoice (to `invoice_xxx.txt`)




