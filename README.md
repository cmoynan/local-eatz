# LocalEatz

![image](https://github.com/user-attachments/assets/dbfe5de9-2c60-4234-af02-bfeb569f26ca)

## Admin Login
**Username**: gitpod 
**Password**: Kildare89

## Overview

LocalEatz is a web application designed to simplify the process of booking tables at people's favorite local restaurants. Users can easily register on the website, book tables, and manage their bookings with ease. Whether it's making a new reservation, editing an existing one, or canceling a booking, LocalEatz provides a seamless experience. The platform also keeps users informed with email notifications for every booking action.

In addition to catering to diners, LocalEatz also offers a Business Enquiry section where restaurant owners and businesses can reach out to list their restaurants on the platform. This feature enables restaurants to grow their customer base by making their dining experiences available to a larger audience looking for convenient booking options.

# Features

## For Users:

### Create an Account
Users can easily create an account on LocalEatz by signing up with their email. The Django Allauth integration ensures a smooth and secure registration process allowing users to either register with their email and password. Once an account is created, users can log in to access all the features on the site. Non users can browse the website but will be prompted to login to make a booking.

![image](https://github.com/user-attachments/assets/47fe3546-cd78-4230-9336-74587210b016)

### Make Bookings

After logging in, users can browse through the available restaurants and make table reservations. They can choose the date, time, and party size, and even provide special requests for a more personalized dining experience. The platform ensures that users can book tables in real-time, receiving immediate confirmation via email.

![image](https://github.com/user-attachments/assets/34f06eea-3d09-4081-ba83-e31d82bbbc7f)

![image](https://github.com/user-attachments/assets/78fa29dc-200b-4ee4-9d00-2ab25d0af4e2)

![image](https://github.com/user-attachments/assets/780ad469-712b-4f94-8a7a-a0e6116d1187)



### Manage Bookings

Once logged in, users have full control over their bookings. They can view all upcoming reservations, and if needed, they can edit or cancel their bookings directly from their dashboard. Whether it’s adjusting the time or canceling a reservation altogether, users can do so with ease.

![image](https://github.com/user-attachments/assets/014dd7bf-ea54-4091-99f7-94ea88ad178e)

![image](https://github.com/user-attachments/assets/d871682f-8600-4b81-9c45-f425bf132ff3)

![image](https://github.com/user-attachments/assets/a51cbeca-ab88-402c-b7d8-c38c3a8eac20)


### Password Reset

In case users forget their passwords, LocalEatz provides a password reset option via Django Allauth. Users can quickly reset their password by receiving a secure password reset link in their email. This ensures that account security and user convenience are prioritized.

![image](https://github.com/user-attachments/assets/f200f1e7-9d89-4244-ad03-644821db4292)

![image](https://github.com/user-attachments/assets/f83cb414-f0bf-4f45-b8c8-9b94ebed8092)

![image](https://github.com/user-attachments/assets/651e7093-daed-4736-b337-b7d55d523d93)


### Business Enquiry

In addition to serving users, LocalEatz also provides a Business Enquiry section where restaurant owners can contact the platform to list their establishments. This feature allows businesses to grow their customer base and make their dining experiences available to a larger audience.

![image](https://github.com/user-attachments/assets/ba33832a-5bdc-4c03-89ca-97aa02b43a4a)

![image](https://github.com/user-attachments/assets/57b6f02d-cb4f-46c5-9051-fdf0b48c2c6f)

## For Admins:

Admin Dashboard: Access a dedicated admin interface.

![image](https://github.com/user-attachments/assets/6aad209f-6aae-4dd9-92eb-e62e015bd197)

### Manage Restaurants

Add Restaurants: Admins can create new restaurant entries, including details such as name, address, description, maximum tables, and cuisine type.
Edit Restaurants: Modify existing restaurant information to ensure data accuracy.
Delete Restaurants: Remove outdated or duplicate restaurant entries.

![image](https://github.com/user-attachments/assets/5315d258-84d0-488f-a96e-e9d1729090a6)

![image](https://github.com/user-attachments/assets/6728aee7-ec3a-4542-9a7a-0ecea48b5cb5)

![image](https://github.com/user-attachments/assets/b92d1521-07b1-4313-a5b2-2c9407a5822b)

 ### Manage Bookings
 
View Bookings: See all reservations made by users in a clear and organized list.
Edit Bookings: Update booking details, such as the party size, date, or time, in case of user requests or conflicts.
Delete Bookings: Cancel bookings directly from the admin interface.

![image](https://github.com/user-attachments/assets/8800329a-a8c0-4e44-a6db-8cfd8dfe0b3e)

![image](https://github.com/user-attachments/assets/f587b557-6ccf-4a6e-bcfc-0845eb344790)

### View Customer Inquiries

Access Inquiries: View all customer inquiries submitted through the contact form. Each inquiry includes the customer's name, email, and message, along with the date of submission.
Track Messages: Quickly address user questions or concerns by reviewing inquiries in the admin dashboard.

![image](https://github.com/user-attachments/assets/03d5c3f8-6976-4adb-a8a1-ab0abd72fb0a)

![image](https://github.com/user-attachments/assets/2d4485f6-f0a9-4f8c-ad62-4e9eef44986a)

### 4. View Business Inquiries
Access Business Requests: See inquiries from local businesses interested in listing their restaurants on the platform.
Facilitate Communication: Respond to potential business partners through their provided contact details.

![image](https://github.com/user-attachments/assets/aca1a8d9-598e-48b8-a4d7-4a7e321a00b9)

![image](https://github.com/user-attachments/assets/c14bb28c-7f32-46c7-b9e8-d89ebe549389)

# Authentication

## Form Authentication

### Registration

For my application, email addresses are a mandatory part of the user setup process. This ensures that users receive important emails regarding any changes to bookings. During registration, users must provide a valid email address, which is used for email verification and other account-related notifications. At sign up if users try to regsiter with an invalid email address they will be notified

![image](https://github.com/user-attachments/assets/b4934331-0361-4aa1-a4d7-b4a5569768be)

## Bookings

### Time Slot Availability

Users are presented with a dynamic list of available time slots for bookings.

![image](https://github.com/user-attachments/assets/6218b0b7-b29b-4beb-9aa7-50712e248e5e)


If the number of bookings at a particular time exceeds the restaurant’s maximum table capacity, the system automatically removes that time slot from the available options.
This ensures users can only select time slots that are available, reducing the chance of overbooking.

If a user selects a time slot that becomes fully booked before their submission is processed, they are notified with a message indicating the unavailability:
"The selected time is fully booked. Please choose a different time."
This real-time validation helps maintain fairness and avoids conflicts in scheduling.

![image](https://github.com/user-attachments/assets/03c29e24-8714-4fd2-97bd-f59fb3baf5e8)


### Past Date and Time Validation

The system prevents users from booking a table in the past.
If a user attempts to choose a past date or time, they receive a clear error message:
"You cannot book a table in the past. Please choose a valid time."
This ensures all bookings are made for valid future dates and times.

![image](https://github.com/user-attachments/assets/07e2302a-bf94-4669-afd8-7480dcbbd153)

## User Notifications with Messages

LocalEatz uses Django's built-in messaging framework to provide real-time feedback to users for various actions performed on the platform. This ensures that users are always informed about the status of their actions, enhancing their overall experience.

### Signing In and Signing Out

Upon logging into their account, users see a welcome message which also advise's of their username:

![image](https://github.com/user-attachments/assets/05a65a6a-42e2-428b-8851-f857a6e463be)


When signing out they also get a message that they have signed out:

![image](https://github.com/user-attachments/assets/802bf380-e6f6-45c9-aab3-792514b928a2)

### Making a Booking

Upon successfully booking a table, users see a confirmation message:

![image](https://github.com/user-attachments/assets/ab9ad959-9403-4c66-bb9a-9f0995214594)


### Editing a Booking

After updating their booking details, users receive a success message:

![image](https://github.com/user-attachments/assets/48cc8d5c-29d4-4e39-ad0f-b49926560e8e)

### Cancelling a Booking

When a user cancels a booking, a success message confirms the cancellation but they also require to confirm cancellation to avoid any mistakes/errors in cancelling:

![image](https://github.com/user-attachments/assets/1fa4ac8a-b8b8-4d1c-b46a-fbecbbdd1d7c)

![image](https://github.com/user-attachments/assets/720cbbe2-13d7-4985-bc6c-c64841e9d11a)

# Design Overview

## Minimalistic and User-Friendly Approach
The design of this application is centered around minimalism and usability. Key aspects include:

### Clean Aesthetic: 
The design uses a dark background with light text  to create a high-contrast, easy-to-read interface. This not only enhances readability but also provides a sleek, modern look.

### Consistent Color Scheme:
A vibrant pink is used as the primary color for buttons, headers, and other interactive elements. This choice adds a touch of personality and visual interest, while ensuring that key actions and elements stand out.

### Fixed Navigation: 
The header and footer are fixed, providing constant access to navigation and important information without scrolling. This design choice enhances usability and keeps essential elements within easy reach. On mobile screens the nav bar is hidden behind  a menu icon which users can collape to use the navigation options.

![image](https://github.com/user-attachments/assets/73aba96f-25bd-4aa9-8278-1dea895f6e66)

![image](https://github.com/user-attachments/assets/2198161e-aff1-4913-80c8-599aa95029a1)



### Responsive Design: 
Media queries and bootstrap styling ensure the application is accessible and visually appealing across various devices, from mobile phones to large desktop monitors. This includes adjustments to padding, font sizes, and layout to accommodate different screen sizes.


### Interactive Elements:
Buttons and interactive elements feature smooth transitions and hover effects to enhance user engagement and provide visual feedback. This makes the application feel more dynamic and responsive.

Overall, the design focuses on simplicity and ease of use, creating an intuitive and aesthetically pleasing user experience.

## CRUD Functionality

### User CRUD Operations
Users of the LocalEatz platform can perform the following CRUD (Create, Read, Update, Delete) operations related to bookings:

1. **Create a Booking**:
   - Users can create a booking at a restaurant by selecting a date, time, and party size. The available time slots are dynamically updated based on the restaurant's table availability.
   - If a user tries to book a table for a past date or time, they are notified that the booking is not allowed.
   - If the restaurant has already reached its maximum table capacity for the selected time, the time slot will be removed from the available options, and the user will be informed.

2. **View My Bookings**:
   - Users can view their current and past bookings, including details such as restaurant name, booking time, party size, and any special requests.
   - The booking details are displayed in a user-friendly manner, and users can access this section from their account dashboard.

3. **Edit a Booking**:
   - Users can edit their bookings if needed, including changing the date, time, party size, or contact information. However, they cannot set a past date or time for the booking.
   - If a user tries to change the booking to a time that exceeds the restaurant’s table capacity, they are notified and prompted to choose a different time.

4. **Cancel a Booking**:
   - Users can cancel their bookings if they no longer need the reservation. Upon cancellation, the user receives a confirmation message, and the booking is removed from the system.

### Admin CRUD Operations
Admins have full CRUD access to manage restaurants, bookings, and customer inquiries. In addition to the operations available to regular users, admins can:

1. **Manage Restaurants**:
   - **Create Restaurants**: Admins can add new restaurants to the system, including the name, address, description, cuisine type, and maximum number of tables.
   - **Edit Restaurants**: Admins can update restaurant information, such as changing the name, address, cuisine type, or the maximum number of tables available.
   - **Delete Restaurants**: Admins can delete restaurants from the system. All related bookings and inquiries will also be removed upon deletion of the restaurant.

2. **Manage Bookings**:
   - **View All Bookings**: Admins can view all bookings made by users, including details such as the user’s name, booking date, time, and party size.
   - **Edit Bookings**: Admins can edit any booking, adjusting details like the booking time, party size, or restaurant.
   - **Delete Bookings**: Admins can delete bookings if required, freeing up restaurant space for other users. A confirmation message will be shown after the deletion.

3. **View and Manage Customer Inquiries**:
   - **View Customer Inquiries**: Admins can view any customer inquiries submitted through the contact form. These inquiries can include questions, complaints, or feedback about the restaurants or services.
   - **Delete Inquiries**: Admins can delete any customer inquiries once they have been addressed or resolved.

By providing these functionalities, the system supports a seamless user experience for customers while giving admins full control over restaurant and booking management.

# Automated Tests Overview

![image](https://github.com/user-attachments/assets/02f1b2b8-8463-4114-8a4b-4c1f97dd0f19)


LocalEatz leverages Django’s built-in testing framework to ensure the robustness and correctness of its features. The following sections outline the key tests that were carried out to validate different functionalities of the platform.

### Restaurant List and Details

#### RestaurantListTest:

This test ensures that the restaurant list page displays correctly. It validates that the user can access the restaurant list after logging in and checks if the restaurant information, such as the name, is included in the response.

#### RestaurantDetailTest:

This test checks the restaurant detail page to ensure it correctly displays details of a specific restaurant, including its name, address, and other relevant information.

### Booking Creation and Validation

#### CreateBookingTest:

This test validates the booking creation process. It checks that users can successfully create a booking for a future date and time. It also checks how the system responds to invalid data, such as selecting a past date, ensuring proper error handling is in place.

### User's Bookings Management

#### MyBookingsTest:

This test ensures that users can view their bookings after logging in. It also tests the ability to cancel a booking and edit it. The test checks if the correct data is reflected after the booking is updated or canceled, ensuring that users can modify their bookings correctly.

### Booking Editing

#### test_edit_booking_valid_data:

This test ensures that users can edit their bookings with valid data. It checks that the booking is successfully updated, and the system correctly redirects the user upon a successful update.

#### test_edit_booking_invalid_data_past_date:

This test ensures that the system prevents users from editing their booking with a time in the past. It verifies that the booking data is not updated and the user receives a validation message when attempting to choose an invalid time.

#### Additional Validations
The tests also cover validation for other important aspects of the booking process, such as:

##### Date and Time Validation: 

Ensuring users cannot book a table in the past.

##### Maximum Table Capacity: 

Validating that bookings cannot exceed the maximum table capacity of a restaurant at a given time.

All tests are executed using Django's TestCase class, which provides a convenient way to simulate requests to views, interact with the database, and assert expected outcomes. The tests ensure that critical paths such as booking creation, viewing and editing bookings, and canceling bookings work correctly under normal and edge cases.

By running these automated tests, LocalEatz ensures that the system behaves as expected and that users have a smooth experience when interacting with the platform.

# Manual Tests Overview

The following manual tests were conducted on the LocalEatz platform to ensure that users can interact with the system smoothly and that all functionalities work as intended. The tests cover the key user interactions such as account management, booking creation, and viewing, editing, and canceling bookings.


#### Manual Test Table

| **Test Case**                               | **Description**                                                                                        | **Expected Outcome**                                                                                     | **Result**  |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-------------|
| **1. Account Registration**                | Test the process of registering a new user account using the registration form.                         | User is able to create a new account and receives a confirmation message.                                 | Passed      |
| **2. User Login**                          | Test logging in with a valid username and password after account creation.                             | User successfully logs in and is redirected to the home page.                               | Passed      |
| **3. User Login with Invalid Credentials** | Test login with incorrect username or password.                                                        | User receives an error message indicating invalid credentials.                                            | Passed      |
| **4. Password Reset**                      | Test the password reset functionality by requesting a password reset email and following the link.     | User receives a reset email and can successfully reset their password.                                    | Passed      |
| **5. Booking Creation (Valid Data)**       | Test booking a table with valid data (restaurant, date, time, party size).                              | Booking is successfully created, and user is shown a success message.                                     | Passed      |
| **6. Booking Creation (Past Date)**        | Test booking a table for a past date.                                                                   | System prevents the booking, showing an error message that bookings for the past are not allowed.        | Passed      |
| **7. Booking Creation (Invalid Time)**     | Test booking a table for a time when the restaurant has no available tables (i.e., exceeds capacity).   | System prevents the booking and shows a message indicating that the maximum table capacity is reached.    | Passed      |
| **8. Edit Booking (Valid Data)**           | Test editing an existing booking with valid data (e.g., changing the time, party size, or contact info).| Booking is successfully updated and user is shown a success message confirming the changes.              | Passed      |
| **9. Edit Booking (Past Date/Time)**       | Test editing a booking to set a time in the past.                                                       | System prevents the change, showing a message that past times cannot be selected.                        | Passed      |
| **10. Cancel Booking**                     | Test canceling an existing booking.                                                                     | Booking is successfully canceled and user is shown a confirmation message.                                | Passed      |
| **11. View Bookings (Logged In User)**     | Test the view bookings page, ensuring that the logged-in user can see their bookings.                   | User sees a list of their current bookings, with the ability to view details, edit, or cancel bookings.   | Passed      |
| **12. View Restaurant Details**            | Test viewing a restaurant's details page (e.g., address, available tables, cuisine).                    | User can view the details of the restaurant, including availability, address, and description.            | Passed      |
| **13. Log Out**                            | Test logging out of the user account.                                                                   | User is logged out successfully and redirected to the home page.                                         | Passed      |
| **14. Business Inquiry**                   | Test submitting a business inquiry through the contact form.                                           | User receives a success message confirming that their inquiry has been sent.                             | Passed      |

#### Test Description
- **Account Registration**: Verifies that users can create an account using the registration form, entering all necessary fields (name, email, password, etc.).
- **User Login**: Confirms that users can log into their account using correct credentials.
- **Password Reset**: Tests the ability to reset a forgotten password by receiving an email with instructions.
- **Booking Creation**: Ensures users can book tables for a valid date, time, and party size at the restaurant.
- **Booking Editing**: Validates that users can edit their bookings, such as changing the date, time, or party size.
- **Booking Cancellation**: Ensures that users can cancel their bookings.
- **Viewing Bookings**: Verifies that users can view all their bookings and manage them effectively.
- **Business Inquiry**: Ensures that restaurant owners or managers can submit inquiries through the contact form to list their restaurant on the platform.

## Performance Testing

Ensured pages load quickly and efficiently.  Cross-Browser Compatibility Verified consistent look and feel across all tested browsers. Ensured all interactive elements function correctly in each browser. Ran Lighthouse on devtools to get a performance score.

![image](https://github.com/user-attachments/assets/57470a1f-5bdf-45f1-a6bc-947002e926a6)

## CSS Validator

![image](https://github.com/user-attachments/assets/753895aa-3f85-4696-a830-4c44762d282e)

# Database Schema and Relationships

![image](https://github.com/user-attachments/assets/ac76bd77-5bd8-4766-b617-193762027037)

### Restaurant Model:

Has basic fields like name, address, description, max_tables, and cuisine_type
One restaurant can have many bookings (one-to-many relationship)


### User Model (Django's built-in auth.User):

Contains standard user fields (username, email, password)
One user can have many bookings (one-to-many relationship)


### Booking Model:

Acts as the junction between Restaurant and User
Contains booking-specific information (date, time, party size, etc.)
Has foreign keys to both Restaurant and User
Includes timestamps for creation and updates



### The relationships are:

Restaurant → Booking: One-to-many (one restaurant can have multiple bookings)
User → Booking: One-to-many (one user can have multiple bookings)

# Known Bugs

### Email Registration Bug:

Users can currently sign up with an email that is already registered on the platform. Although an email notification is sent stating that an account is already registered with the provided email, the issue of being unable to register with a duplicate email has not been resolved on the registration page.

**Status**: Due to time constraints, this issue remains open and has not yet been fixed.

### Styling Issues on Certain Devices:

Some styling issues may occur on certain devices. These issues primarily involve layout and visual elements that do not render as expected. However, these styling inconsistencies do not interfere with the overall functionality of the website.

**Status**: While these issues are recognized, they do not affect the user experience significantly, and they are marked for future improvements.

# Future Plans

As LocalEatz continues to grow and more restaurants join the platform, several exciting features and improvements are planned to enhance user experience and provide more value to both users and restaurant partners.

### Enhanced Search Functionality

To help users find the perfect dining experience, we plan to implement advanced search criteria, including:

#### Location-Based Search:

Users will be able to search for restaurants based on their location, making it easier to find nearby dining options.

#### Cuisine Type:

Users will have the ability to filter restaurants by cuisine type, such as Italian, Chinese, Indian, etc., to match their culinary preferences.

#### Rating System

Introducing a rating system will allow users to provide feedback on their dining experiences and help others make informed decisions. Key features include:

#### User Ratings and Reviews:
Users will be able to rate restaurants on a scale (e.g., 1 to 5 stars) and leave detailed reviews.

#### Search by Popularity:
The search functionality will include options to filter and sort restaurants based on their ratings and popularity, highlighting top-rated establishments.

### Restaurant Menus
To assist users in making decisive choices when picking a restaurant, we will add the functionality to display restaurant menus. This feature will include:

#### Menu Listings:

Restaurants will have the option to upload their menus, including details on dishes, prices, and specials.

#### User Interaction:

Users can browse menus before making a reservation, ensuring they select a restaurant that meets their dietary preferences and budget.

# Agile Development Approach

https://github.com/users/cmoynan/projects/7


### Kanban Board

The development of LocalEatz followed the Agile methodology, specifically utilizing the Kanban board for task management. The Kanban board allowed me to manage tasks effectively by categorizing them into different stages, ensuring a smooth and efficient development process.

The Kanban board was structured with the following columns:

**To-Do**: Tasks that were ready to be worked on and prioritized for the current sprint.
**In Progress**: Tasks that were actively being worked on by the development team.
**Done**: Tasks that had been reviewed, tested, and fully completed.

This approach helped me visualize the development flow, track progress in real-time, and adjust priorities as needed.

### MoSCoW Prioritization

To ensure that the most important features were developed first, the MoSCoW method was used to prioritize tasks.


![image](https://github.com/user-attachments/assets/d2905e9f-cdff-41d0-9bbd-32e557e27a2b)

# Cloning and Forking the Project from GitHub

To get a copy of the **LocalEatz** project up and running on your local machine, follow these steps:

### Cloning the Repository

1. **Navigate to the GitHub Repository:**
   Go to the GitHub repository page for LocalEatz:  
   [https://github.com/cmoynan/local-eatz](https://github.com/cmoynan/local-eatz)

2. **Clone the Repository:**
   - Click on the **"Code"** button on the repository page.  
   - Copy the HTTPS or SSH URL provided.  

3. **Open Your Terminal:**
   Open your terminal or command prompt on your local machine.

4. **Run the Clone Command:**
   In the terminal, run the following command:  
   ```bash
   git clone https://github.com/cmoynan/local-eatz.git

5. **Navigate to the Project Directory**:
    After cloning, move into the project directory:
    cd local-eatz


### Forking the Repository

If you'd like to contribute to the repository or create a personal copy, you can **fork** the repository.

1. **Navigate to the GitHub Repository:**
   Go to the GitHub repository page for **LocalEatz**:  
   [https://github.com/cmoynan/local-eatz](https://github.com/cmoynan/local-eatz)

2. **Fork the Repository:**
   - Click the **"Fork"** button in the top-right corner of the repository page.  
   - This will create a copy of the repository under your own GitHub account.

3. **Clone Your Forked Repository:**
   - Go to your GitHub profile and find your **forked** repository.  
   - Click on the **"Code"** button on your forked repository page.  
   - Copy the HTTPS or SSH URL provided.

4. **Open Your Terminal:**
   Open your terminal or command prompt.

5. **Run the Clone Command:**
   In the terminal, run the following command, replacing the URL with the one you copied:  
   ```bash
   git clone https://github.com/your-username/local-eatz.git

6. **Navigate to the Project Directory**:
   After cloning, navigate to the project directory:
   cd local-eatz

# Deploying the Project to Heroku

#### 1. **Logged In to Heroku:**
   - Logged into my Heroku account and created a new app.  
   - Chose the **Europe region** for my app.

#### 2. **Connect to GitHub:**
   - Linked my Heroku app to my GitHub repository.  
   - Deployed the branchy.

#### 3. **Configure Static Files:**
   - Initially added  `DISABLE_COLLECTSTATIC` as a config variable to handle static files during deployment:

#### 4. **Update settings.py:**
   - Added Heroku to the `ALLOWED_HOSTS` in my `settings.py` file:
    
     
#### 5. **Installed Required Packages:**
   - Installed the following packages for Heroku deployment:
      gunicorn whitenoise psycopg2
     

#### 6. **Created a Procfile:**
   - In my project I created a `Procfile` in the root directory with the following content:
     web: gunicorn localeatz.wsgi
     

#### 7. **Set Debug Mode:**
   - Ensured that `DEBUG` was set to **False** in my `settings.py` to configure the app for production:

#### 8. **Finalize Deployment:**
   - After the initial deployment, you can remove the `DISABLE_COLLECTSTATIC` config variable:
     - **DISABLE_COLLECTSTATIC = 0**

#### 9. **Generated and Securely Stored the Django Secret Key:**
 Final step to take was I generated a secret key and hid the secret key in an environment variable

#### 10. **Config Variables:**

![image](https://github.com/user-attachments/assets/578d81fc-7a98-4342-a9b4-beef6bbc71b8)


### Heroku deployed app:

https://local-eatz-f0cecf1cc4fa.herokuapp.com/

### Github Repo :

https://github.com/cmoynan/local-eatz
   















