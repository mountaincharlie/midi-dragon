# Midi Dragon [TO FINISH]

Midi Dragon is an ecommerce web application for users who want to design their own custom songs or short music clips, which are then created for them. From YouTubers looking for an intro song to capture the essence of their channel, to hobby video makers in need of a specific sound for their content, Midi Dragon’s choice of pre-made and custom songs is the perfect way for creators to find authentic sound for their projects. 

This application provides users with the ability to browse a collection of pre-made songs or design their own custom project with our simple form which they canview, edit and delete in their profile dashboard, up until they decide to purchase it. Testimonials from previous successful projects are available for users to get a feel for what Midi Dragon can create for them. Customers who are happy with their own custom songs have the option to allow their song to be used as a testimonial to promote their own platforms and content as well as reviewing Midi Dragon’s services.

### Deployed Site link
* [midiDRAGON](https://midi-dragon.herokuapp.com/)

![Viewing midiDRAGON on desktop](./static/images/readme_images/midi-dragon-desktop-view.png "Viewing midiDRAGON on desktop")
![Viewing midiDRAGON on mobile](./static/images/readme_images/midi-dragon-mobile-view.png "Viewing midiDRAGON on mobile")


## Contents [TO FINISH]
---
* [Business Model](https://github.com/mountaincharlie/project-five-midi-dragon#business-model)
* [Marketing Strategy](https://github.com/mountaincharlie/project-five-midi-dragon#marketing-strategy)
* [Search Engine Optimisation](https://github.com/mountaincharlie/project-five-midi-dragon#search-engine-optimisation)
* [Technologies Used](https://github.com/mountaincharlie/project-five-midi-dragon#technologies-used)
* [Frameworks Libraries and other Applications Used](https://github.com/mountaincharlie/project-five-midi-dragon#frameworks-libraries-and-other-applications-used)
* [Project Management](https://github.com/mountaincharlie/project-five-midi-dragon#project-management)
* [Initial Designs](https://github.com/mountaincharlie/project-five-midi-dragon#initial-designs)
* [Database Schema](https://github.com/mountaincharlie/project-five-midi-dragon#database-schema)
* [Final Designs](https://github.com/mountaincharlie/project-five-midi-dragon#final-designs)
* [User Experience Design](https://github.com/mountaincharlie/project-five-midi-dragon#user-experience-design)
* [Accessibility](https://github.com/mountaincharlie/project-five-midi-dragon#accessibility)
* [Commit Messages](https://github.com/mountaincharlie/project-five-midi-dragon#commit-messages)
* [Testing](https://github.com/mountaincharlie/project-five-midi-dragon#testing)
* [Bugs](https://github.com/mountaincharlie/project-five-midi-dragon#bugs)
* [Deployment](https://github.com/mountaincharlie/project-five-midi-dragon#deployment)
* [Credits](https://github.com/mountaincharlie/project-five-midi-dragon#credits)
* [Future Features](https://github.com/mountaincharlie/project-five-midi-dragon#future-features)



## Business Model [TO FINISH]
---

* Purpose: Business to Consumer (B2C)
  * midiDRAGON is the business, our Pre-made songs are our product, the Custom Songs feature is a service we provide and the users who are purchasing these songs, directly from us, are the consumers.

* Core business intents:
  * The purpose of midiDRAGON is to provide royalty free music that users can purchase once and use for any of thier content creation or personal projects as much as they want. In the case of the Custom Song Design feature, midiDRAGON also allows users to purchase bespoke songs to be made for them.
  * midiDRAGON sells both products and services. The Pre-made Songs are available to be viewed, listened to and purchased by any site users, even if they're not logged in or have an account.The Design a Custom Song service is only available to users who have an account and are logged in, because registered users have access to their Profile Dashboard which is where their draft, in progress and completed Custom Song projects can be viewed and managed. 
  * midiDRAGON makes money via single payments from ts products and services.
  * midiDRAGON is promoted via its Facebook business page (linked in the Marketing Strategy section below), as well as by users who choose for their custom songs to be used as a testimonial on the site, which further promotes midiDRAGON's services to users who are already on the site.
  * The target audience for midiDRAGON are people who are in need of music that is safe for them to use on their personal or professional audio or video creations, but particularly those who are regular content creators (e.g. Youtubers, Podcasters, short film directors). Professional content creators appreciate how difficult it can be to get high quality music that suits their project and won't result in it being demonetized or scrutinized legally.  
  * The value that users get from midiDRAGON is the quick, simple and safe process of purchasing songs, the security of knowing that they can use midiDRAGON's songs in any of their projects without the threat of their content being banned (As long as they don't claim the songs as their own intellectual property in any way. Specific guidance for midiDRAGON's Terms of Service are laid out in the FAQs and Terms of Service pages, which are linked below) and the ability to, without any musical skill or equipment, design a custom song to be made for them. 

* Privacy Policy 
  * [midiDRAGON Privacy Policy](https://midi-dragon.herokuapp.com/privacy-policy/)
  * Credit: [Privacy Policy Generator](https://www.privacypolicygenerator.info/) for generating the policy.

* Terms of Service 
  * [midiDRAGON ToS](https://midi-dragon.herokuapp.com/terms-of-service/)

* Frequently Asked Questions 
  * [midiDRAGON FAQs](https://midi-dragon.herokuapp.com/frequently-asked-questions/)


## Marketing Strategy [TO FINISH]
---

* Facebook Business Page
  * [midiDRAGON Facebook Business Page](https://www.facebook.com/Midi-Dragon-107201462130945)
  * ![midiDRAGON Facebook Business Page](./static/images/readme_images/midi-dragon-fb-business-page-1.png "midiDRAGON Facebook Business Page")
  * ![midiDRAGON Facebook Business Page](./static/images/readme_images/midi-dragon-fb-business-page-2.png "midiDRAGON Facebook Business Page")
  * Cover photo matching the mididDRAGON site
  * Profile picture matching the mididDRAGON logo
  * 'Shop On Website' button which takes the user to the browse Pre-made Songs page
  * 'About' description, ink to site, contact email, price range and relevant tags
  * First post to promote the site and including the link to the site

* Email Newsletter Subscription
  * mididDRAGON uses this as their primary marketing strategy since its just a small business starting out at the moment and requires free/low cost marketing.
  * This has been implemented on midiDRAGON's site using [MailChimp](https://mailchimp.com/en-gb/)'s Newsletter Subscription form in the footer.
  * ![Email Subscription Form with MailChimp](./static/images/readme_images/newsletter-with-mailchimp.png "Email Subscription Form with MailChimp")
  * For the purposes of this project, the form is styled to fit the rest of the site and has basic error/success messages powered by MailChimp's code but doesn't actually send any newsletters.

* Content
  * midiDRAGON also slightly implements the Content marketing strategy through the [Testimonials](https://midi-dragon.herokuapp.com/songs/testimonials/) page where users' custom songs are made avaliable for other users to view and listen to, if the user who purchased it allows the song to be used as a testimonial, which helps to promote midiDRAGON's Custom Song service.
  * This is also something that could be expanded in the future to have weekly spotlight songs and other regular content promotion on the site and through the Facebook Page and Newsletter Subscription.
  * Allowing users to leave a link to their own content creation platforms in their testimonials also helps to connect the community and by having it on the midiDRAGON site, this could also motivate people to have their cusomt songs created by midiDRAGON rather than other freelance music producers.


## Search Engine Optimisation [TO FINISH]
---

### Keyword research
* Initial Process
  * Picking 3 main topics and thinking of as many relevant keywords for those topics
  * ![Keyword research Initial list](./static/images/readme_images/kw-research-part-1.png "Keyword research Initial list")
* Stage 2 - using Google search techniques to find more keywords
  * Checking the Google autofill suggestions
  * Adding '_' before the keyword as this acts as a 'wildcard' to give suggestions for additions to the start of the keyword
  * Checking the suggestions at the very bottom of the Google search results page
  * Thinking about the kind of searches that potential midiDRAGON customers would be making (e.g. 'personalised music gifts')
  * ![Keyword research stage 2](./static/images/readme_images/kw-research-part-2.png "Keyword research stage 2")
* Stage 3 - organising the list
  * Removing duplicates and organising clearly
  * ![Keyword research stage 3](./static/images/readme_images/kw-research-part-3.png "Keyword research stage 3")
* Stage 4 - refining the list
  * Considering the __Relevance__ of the keywords - does midiDRAGON's purpose suit the keyword (e.g. 'background music for at home' isn't exactly what midiDRAGON customers are going to be expecting from the site)
  * Considering the __Authority__ midiDRAGON has over the keyword (e.g. most keywords mentioning 'music for Youtube' return a lot of Google searches for services more specific for Youtubers than midiDRAGON)
  * Considering the __Volume__ of searches each keyword gets - and finding a balance between keywords that yield a lot of searches but also that aren't too competitive for a new small business like midiDRAGON
  * Practically, I searched for the keywords in Google and checked which ones didn't appear exactly in too many high ranking site Titles and also which keywords didn't yield too many Google ads as this also was an indication of them not being too competitive. Finally, I considered which keywords were relevant to midiDRAGON's purpose and which midiDRAGON had a reasonable amount of authority over.
  * ![Keyword research stage 4](./static/images/readme_images/kw-research-part-4.png "Keyword research stage 4")

* Choosing the midiDRAGON name
  * midi - Musical Instrument Digital Interface - reffers to the format that most of my music production occurs in
  * dragon - memorable and Font Awesome had a stylish looking icon to act as the logo
  * I researched whether any combinations of midi-dragon existed, but there were no music related results aside from one album name.
  * So midiDRAGON was unique, memorable and relevant enough to work well for the site.

* Semantic HTML
  * Many of the keywords contain the names of the song genres on midiDRAGON (e.g. Lofi, Cinematic, Indie) which appear many times throughout the site.
  * Some of the keywords appear in headings, buttons and the title element across the site (e.g. Pre-made Songs, Design Custom Song)
  * Some of the keywords are mentioned in the FAQs (e.g. Royalty free music, Custom Songs)
  * All of the media files used for the site also have relevant names (e.g. each Pre-made Song's image and audio file has a name to match the name of the song) which improves the SEO for the site.

* meta tags
  * Meta Tag - Filling it with my refined list of keywords.
  * Description Tag - Creating a summary of the site's key features whilst making use of the keywords in my final list.

* Links to reliable and relevant external sites
  * I included links to 2 additional sites in the footer; Heroku (for the creation of the app) and Fl Studio (as the Digital Audio Workspace that I use for creating my music), since these are both reliable and reputable site which are both very relevant to midiDRAGON.
  * For the links to Heroku, FL Studio and my Facebook Business page, I used the target="_blank" attribute in order for them to be opened in a new page when clicked so that the users aren't taken away from midiDRAGON. I also included the rel="noopener noreferrer" attribute to prevent the linked site being able to have any information about or any access to my site through users clicking the link.

* robots.txt file
  * Simple text file elling the Search Engine the urls its not allowed to crawl/index.
  * Its presence in a project shows the Search Engine that you ackowledge it has access to the site and is a sign of quality, improving your ranking.
  * I created the robots.txt file in my root directory including the 'User-agent' as * indicating it applies to all SEO 'agents', listed the 'Disallows' (for my accounts, tracklist and profiles urls) and included my 'Sitemap'

* sitemap.xml file
  * Lists the site's important page urls so that the Search Engine can navigate through them, helping the Search Engine understand the site's structure, speeding up it sprocess and ensuring all the essential pages are covered.
  * I used [xml-sitemaps](https://www.xml-sitemaps.com/) to generate my sitemap.xml file
  * I then made sure I uploaded this into the root directory of my project.


## Technologies Used [TO FINISH]
---
* HTML
* CSS
* Python
* JavaScript


## Frameworks Libraries and other Applications Used [TO FINISH]
---

* Django with;
    * gunicorn
    * psycopg2
    * postgresql
    * AllAuth
    * Crispy Forms
    * django-storages
* Bootstrap
* Stripe
* boto3 (for AWS)


## Project Management [TO FINISH]
---
* Using GitHub
    * link to Midi Dragon Project page

* Using GitHub Projects to create Epics (big features/tasks)
    * screenshot of full list of numbered epics (collapsed)
    * screenshot 

* Using GitHub Issues to create User Stories and Project Maintenance (with GitHub’s labels to identify their type)
    * screenshot of github issue types (e.g. user story with MoSCoW priority labels)

* Using GitHub's Project KanBan board feature to mark my progress throughout the project
    * screenshot of the kanban board for one of the epics

* Using GitHub labels to prioritize User Stories (using MoSCoW prioritization)
    * md syntax for images: (![Project Maintainance label](./static/images/readme_images/proj-maint-label.jpg "Project Maintainance label"))
    * screenshots of all the labels you use, with their definition etc

* Using checklists within the GitHub Issues in order to specify the tasks required to achieve User Stories, Project Maintenance and Testing
    * screenshot of a checklist within a user story/maintenance/testing 


## Initial Designs [TO FINISH]
---

### Header
* For logged in users
  * image
* For non-logged users:
  * image

### Footer
* image

### Landing Page
* image

### Browsing Songs
* image

### Testimonials Page
* image

### Song Details
* pre-made songs image
* custom songs image

### Create/Edit Custom Song Page
* image

### My TrackList Page (user’s ‘basket’)
* image

### Checkout Page
* image

### Order Confirmation Page
* image

### My Profile Dashboard (contains links to Project Drafts, Projects In Progress, Completed Projects, Order History and My Details)
* My Details
  * image
* Project Drafts
  * image
* Projects In-Progress
  * image
* Completed Projects
  * image
* Order History
  * image

### Admin Site Management
* Add Song
  * image
* Add Genre
  * image
* Add Instrument 
  * image
* Custom Songs 
  * image
* All Orders 
  * image

### AllAuth authentication screens
* Login 
  * image
* Register
  * image
* Logout
  * image

### Delete Confirmation Page
* image

### Custom 404 Page
* image

## Database Schema [TO FINISH]
---

### Initial Schema Plan
* A Song table containing the fields:
  * id [automatically increments]
  * name [charField, name of the song]
  * image [imageField, with a placeholder image as a default]
  * audio_video [fileField OR separate audioField and videoField]
  * slug [slugField, auto generated in pre_save() signal as a unique char string]
  * project_type [intField/ForiegnKey, 1-to-many relationship with ProjectType model]
  * owner [intField/ForiegnKey, 1-to-many relationship with Django’s User model]
  * genre [intField/ForiegnKey, 1-to-many relationship with Genre Model]
  * audio_clip [fileField, default:false, optional for users to add their own audio clip for me to use]
  * bpm [intField, beats per minute for the song]
  * song_purpose [textField, part 1 of the song description (broken down to make the form more intuitive)]
  * song_feel [textField, part 2 of the song description (broken down to make the form more intuitive)]
  * additional_details [textField, part 3 of the song description (broken down to make the form more intuitive)]
  * song_end_fade [booleanField, default: true, songs ends by fading to silence rather than ending on a beat/chord]
  * price decimalField [decimalField, max_digits=10, decimals=2, auto generated in pre_save() signal, song is a FK in OrderItems Model so that this value can be used there]
  * use_as_testimonial [booleanField, default: false, whether a song will be used as a testimonial or not]
  * testimonial [textField, optional written feedback/rating if the user is happy for their custom project to be used as a testimonial]
  * completed [booleanField, default: false, applicable for both the user’s custom projects and for pre-made songs that I’m in the process of adding to the site]
  * public [booleanField, default: False, when use_as_testimonial is True but public is False, this indicates that the song is awaiting being used as a testimonial (either while being edited or while waiting for admin approval)]

* An AddOn table containing the fields:
  * id [automatically increments]
  * type [charField, type of addOn]
  * song [intfield, the id of the song it will be applied to]
  * value [charfield, 'instrument' or 'number' (for additional review session)]
  * price [decimalfield, 'calculated from the values defined in settings.py']
  * further_details [textField, for the user to add additional notes about the addOn]  

* A ProjectType table containing the fields:
  * id [automatically increments]
  * name [charField, name of project type]
  * length [charField, possible time range for a song of each type]
  * num_included_instruments [intField, number of instruments included in each project type’s price]
  * num_included_reviews [intField, number of review sessions included in each project type’s price]
  * min_price [decimalField, price of each project type which would be the minimum price for that custom song project - if no additional instruments etc were added]

* An Instrument table containing the fields:
  * id [automatically increments]
  * name [charField, name of the instrument - used in the code]
  * display_name [charField, name of the instrument - displayed to the user]
Due to it's many-to-many relationship with the Song table, there is also an intermediate table ‘Song_Instrument’ connecting the two tables.

* A Genre table containing the fields:
  * id [automatically increments]
  * name [charField, name of the genre - used in the code]
  * display_name [charField, name of the genre - displayed to the user]

* A Like table containing the fields:
  * id [automatically increments]
  * like [charField]
Due to it's many-to-many relationship with the Song table, there is also an intermediate table ‘Song_Like’ connecting the two tables.

* Django's User table:
I used Django’s built in User model to connect to my UserProfile table with a one-to-one relationship and to my Song table with a one-to-many relationship.

* An Order table containing the fields:
  * id [automatically increments]
  * order_number [charField, non-editable and auto-created by pre_save() signal]
  * user_profile [intField, many-to-one relationship with UserProfile, related_name= "my_orders" so that in profile.html, using an “if my_orders" statement, this will check for the orders the logged in user owns]
  * full_name [charField, editable and populated from the user’s profile or the user is required to type it in]  
  * email [emailField, editable and populated from the user’s profile or the user is required to type it in]
  * date [datetimeField, auto created on Order creation when the order is placed and paid for]
  * order_total [decimalField, total cost of the order instance]

* An OrderItems table containing the fields:
  * id [automatically increments]
  * order [intField, many-to-one relationship with Order table, related_name=orderitems. Used to get the purchase date/time of a song (pre-made or custom project) for that user]
  * song [intField, one-to-one relationship with Song, related_name=songitem. Used to get the song details, like price, for the Order instance]
The items in the OrderItems table are essentially order ‘versions’ of songs that are bought, containing all of the song’s details through the relationship with the Song table and the purchase date and order_number etc through the Order table. Used to create each item in the Order history and Order confirmation displays.

* A UserProfile table containing the fields:
  * id [automatically increments]
  * user [intField, one-to-one relationship with Django’s User model]
  * phone_number [charField, optional for user’s to add if they prefer this means of contact for review sessions]

* I used [dbdiagram.io](https://dbdiagram.io/home) to create a visual representation of my database schema
* ![Initial Database Design](./static/images/readme_images/p5-initial-db-schema.png "Initial Database Design")

### Final Database Schema
* Changes
  * Added the quantity field to the SongInstrument model. While refactoring the Song and Instrument models relationship so that songs could have multiple of any particular instrument without having to create duplicates in the Instrument model.
  * Changed the Song model's audio_video field to just be the audio_file field since there wasn't enough need to allow for videos to be playable on the site since the products we are selling are the audio itself.
  * Removed the song_end_fade and audio_clip fields from the Song model as they were features that weren't really necessary for pre-made or custom songs and distracted from the important features on the Custom Design Song form.
  * Removed the AdOns model - this additional functionality was not essential to the site's function and purpose, so I've left it as a possible future feature.
  * Removed the UserProfile model since it ended up only having a 1 to 1 relationship with the Django built in User model and a 1 to many relationship with the Order model, so instead I just related the Django User model and the Order model directly via a 1 to many relationship.
  * Added the created_date field to the Song model so that the users can see in their Profile Dashboard when their projects were created.
* Final Schema diagram, using [dbdiagram.io](https://dbdiagram.io/home)
* ![Final Database Design](./static/images/readme_images/p5-final-db-schema.png "Final Database Design")


## Final Designs [TO FINISH]
---

(just decsriptions for features - dont need screenshots for every feature as these will be covered in the Testing section)

### Header
* For logged in users
  * screenshots (desktop and mobile)
* For non-logged users:
  * screenshots (desktop and mobile)
* Description of features
  * Nav icons (tracklist has title attribute since it doesnt have a label to say what it is)
  * Admin Site Management option
  * clickable logo
  * search functionality
  * filter options
* Changes from initial design:
    * list any

### Footer
* screenshots (desktop and mobile)
* Description of features
  * MailChimp Newsletter
  * ?? Links to reliable sites (e.g. Heroku and FL Studio?)
  * FB business link
  * Privacy Policy [just screenshot in final designs?]
  * Terms of Use [just screenshot in final designs?]
* Changes from initial design:
  * list any

### Landing Page
* Desktop and mobile final designs
    * desktop screenshot
    * mobile screenshot
* Description of features
  * Informational text
  * b.g. image (fits colour scheme) 
  * Browse Now btn
  * Custom song form btn
* Changes from initial design:
    * list any

### Browsing Songs
* Desktop and mobile final designs
    * desktop screenshot
    * mobile screenshot
* Description of features
   * Search filtering options
   * Number of songs found
   * Song layout/audio controls/details
   * Cursor/song highlight styling makes it clear that the song is a clickable link to its details page
   * Back To Top btn (used across site)
* Changes from initial design:
    * list any

### Testimonials 
* Desktop and mobile final designs
    * desktop screenshot
    * mobile screenshot
* Description of features
   * Carousel with captions/controls/indicators
   * Each image is clickable link to the song's details page
   * BS cards for all testimonials (below carousel)
* Changes from initial design:
  * list any

### Song Details (for all song types)
* Desktop and mobile final designs
  * desktop screenshot
  * mobile screenshot
* Description of features
  * if the user has a song in their Tracklist, instead of being able to purchase the item again there is a note to say this is in their Tracklist already
  * if the user have already bought the item (it’s in one of their orders) then theres a message to say that they already own this product and can find it in their profile
  * for purchased custom songs which aren't complete there is a note to say where the song will be downloadable from and playable from when complete 
  * for purchased custom songs that are complete there is a Download btn and the audio controls to play the song on site
  * for custom songs which have not yet been purchased, the user has Edit (only some details)/Delete btns
  * for any song complete or not, the admin has access to the Edit (full details)/Delete btns
  * if the song has 'use_as_testimonial' = True, then there is a section to include the testimonial text and a link to the testimonials page ('see other testimonials')
* Changes from initial design:
    * list any

### Create Custom Song
* Desktop and mobile final designs
    * desktop screenshot
    * mobile screenshot
* Description of features
  * fields avaliable for the user to set and their types ... 
  * Included instruments and review sessions are determined by project type
  * Live price calc as options change (add 'affects-price' class to fields which affect the price and put a JS change event listener on them?) [this is just displayed to the user, the real price is calculated in DB so that the user cant affect the price with JS]
  * Add additional instrument and review sessions btn
  * Notes to user
  * cancel and save btns
* Changes from initial design:
    * list any

### Edit Custom Song
* Desktop and mobile final designs
    * desktop screenshot
    * mobile screenshot
* Description of features
  * User's can only edit custom songs which they havent bought yet
  * Users can only edit the details which were avaliable to them in their Create Custom Song form
  * delete btn along with the cancel and save btns
* Changes from initial design:
    * list any

### Delete Confirmation Page (used for any deletion confirmation)
* Desktop and mobile final designs
    * desktop screenshot
    * mobile screenshot
* Description of features
  * has cancel btn (which redirects to where the user came from?)
  * note to user
  * delete btn to permenantly delete the object
* Changes from initial design:
    * list any

### My TrackList Page (user’s ‘basket’)
* Desktop and mobile final designs
    * desktop screenshot
    * mobile screenshot
* Description of features
  * each song listed with their appropriate details
  * each song's image and name is a clickable link to its song details page
  * 'remove from tracklist' btn for each song
  * Total Price calcualted in DB
  * Keep Browsing (More Music?) and Secure checkout btns
* Changes from initial design:
    * list any

### Checkout Page
* Desktop and mobile final designs
    * desktop screenshot
    * mobile screenshot
* Description of features
  * Order overview 
  * User's details form
  * Stripe payment form [give Stripe card test details]
  * notes to the user about their email address and the amount their card will be charged
  * My Tracklist and Complete Order btns
  * Processing payment overlay screen [include screenshots]
* Changes from initial design:
    * list any

### Order Confirmation Page
* Desktop and mobile final designs
    * desktop screenshot
    * mobile screenshot
* Description of features
  * note for which email the confirmation will be sent to (the one provided in the form - not necessarily the one the user has in their profile)
  * Order info
  * Order overview
  * User's details from the checkout form
  * Order total
  * Browse More Songs/More Music btn
* Changes from initial design:
    * list any

### My Profile Dashboard (contains links to Project Drafts, Projects In Progress, Completed Projects, Order History and My Details)
(only accessible by the user owning the page - its their profile which is used to populate the data anyway)
* Desktop and mobile final designs
    * desktop screenshots for each screen
    * mobile screenshots for each screen
* Description of features
  * My Details page with form to update the user's full name and email address
  * Project Drafts page listing all of the user's un-purchaseed custom songs, in date order - each song is a clickable link to its details. Also has a btn to create a new custom song?
  * Projects in Progress page listing all of the user's purchased custom songs which have not yet been completed, in date order - each song is a clickable link to its details
  * Completed Projects page listing all of the user's purchased custom songs which have been completed, in date order - each song is a clickable link to its details
  * Order History page listing all of the user's orders in date order - each order number is a toggle to display the order overview OR a link to a Order Overview page (same template as Order Confirmation)
* Changes from initial design:
  * list any

### Admin Site Management (contains adding forms for Song, Genre and Instrument models)
only for admins (protected in views.py)
* Desktop and mobile final designs
  * desktop screenshots for each screen
  * mobile screenshots for each screen
* Description of features
  * Add Song page with a form for the Admin to create a new song in the DB
  * Custom Songs page listing all of the purchased custom songs by any user, in date order (filter by user and In-progress/completed checkboxes for filtering) - each song is a clickable link to its details (where admin can update the testimonial and completed/public fields and upload the audio file)
  * All Orders page listing all of the orders for any user in date order - each order number is a toggle to display the order overview OR a link to a Order Overview page (same template as Order Confirmation) (filter by user)
  * Add Genre form (or might be Future Feature)
  * Add Instrument form (or might be Future Feature)
* Changes from initial design:
  * list any (prioritising Custom Songs and All Orders screens over Add Genre/Instrument)

### Admin Edit Song
If the logged in user is the admin then a different view class is called whenever the Edit btn is selected since the admin can access/edit **any** field 
* Desktop and mobile final designs
    * desktop screenshot
    * mobile screenshot
* Description of features
  * for any song the admin can edit any of its fields 
* Changes from initial design:
    * list any

### AllAuth authentication screens (login/out, register, email confirmation sent)
* Desktop and mobile final designs
  * desktop screenshot
  * mobile screenshot
* Description of features
  * link from login page to register page if the user doen't have an account yet
  * link from register page to login page if the user already has an account
  * Back To The Music btn on logout page
* Changes from initial design:
  * list any

### Custom 404 Page
* Desktop and mobile final designs
    * desktop screenshot
    * mobile screenshot
* Description of features
  * Note to user
  * same b.g. image as landing page
  * Take Me Back To The Music btn
* Changes from initial design:
    * list any

## User Experience Design [TO FINISH]
---

### Mobile First Design With Bootstrap 5
* In order to make my site responsive across different screen sizes, I used Bootstrap's [Grid System](https://getbootstrap.com/docs/5.0/layout/grid/) to make use of its ability to rearrange columns on the screen depending on its screen size.
* Examples of how this was useful/appeared to the user ...

### Consistency
* Making use of Django as a templating language by creating a base.html file with title_extra, header, main and footer sections to be used across all pages and a toasts_base.html for consistency across my BS toasts.
* Each of the template html files also follow Bootstraps grid system to keep them responsive and a familiar look across the pages.
* I used primarily bootstrap classes for styling so that the layout is familiar across the whole site and created a number of custom color and background-color styles which i reused across the site similarly to how bootstrap classes are applied.
* Each page also has the same font for headings and for other text content so this also remains consistent throughout the site.
* Deciding on colour scheme at the start inorder to write style rules to implement early on and to be able to create a landing page image with the same colours used throughout the site (e.g. creating teal-btn, grey-btn and red-btn to define the 3 btn types and all of them highlight in pink on hover/selection)

### Specific Feedback Messages To Users 
* e.g Successful signup/login message:
    * screenshot

### Navigation
* The site logo is a clickable link back to the homepage.
* The footer across all pages contains the link to the Facebook business page, the MailChimp email subscription form and the link to the Privacy Policy document.
* Features such as the searchbar, genre/song types search selections, My TrackList, Profile/Login and Logout/Register links are available in the header in all pages, so the user doesn't have to go anywhere specific in order to use these features.
* Return buttons so that the user can navigate easily from their search results back to where they made the search.
    * screenshots
* Cancel button on Create Project, Edit Project and Delete Project confirmation pages so that the user doesn't have to use the browsers back button in order to cancel out of any of these pages.
    * screenshots


## Accessibility [TO FINISH]
---

### Lighthouse Accessibility Score
* screenshot

### Semantic Elements
* Using 'header', 'nav', 'main' and 'footer' in base.html to make the roles of each section obvious.
* Adding role="button" for link elements which are being used as buttons

### Aria-Labels
* Added aria-labels to all link and button elements


## Commit Messages [TO FINISH]
---

* After receiving positive feedback on the organization and consistency of my Git Commit messages on my last project, I decided to use [Conventional Commit’s](https://www.conventionalcommits.org/en/v1.0.0-beta.2/) recommended commit message structure again. 
* I used a mixture of their recommended Types and some of my own:
    * feat - new feature
    * fix - bug fixes
    * docs - documentation only changes
    * style - changes not affecting the code meaning (e.g. removing blank lines)
    * refactor - code change which isnt a fix or feature
    * test - adding a missing/correcting an existing test
    * chore - changes not affecting the source or test file (e.g. deleting unwanted files)
    * setup (custom type) - installing dependencies and adding setup code for them
* They also suggested using square brackets after the Type to add an optional Scope, which would be the thing that the commit applies to, if necessary.
* The commit messages follow the structure:
    * "type[optional scope]: commit description"


## Testing  [TO FINISH]
---

* show manual testing for features like (messages to user if they have already bought a song or it's in their Tracklist already)

### Automated Testing with Django
(IS THIS STILL NECESSARY IF YOU HAVE THE IF STATEMENT FOR DEVELOPMENT MODED?)
* In order to run these tests, I needed Django to use sqlite3 as a local database. To do this I created a 'TESTING' variable in my env.py file and then in settings.py I added an If Statement which checked for this variable and used the sqlite3 database if it was found. When I was not running tests, I commented out this variable and so Django instead used my postgresql database.
    * in my env.py:
    * ![env.py var for testing](./static/images/readme_images/testing_mode_env.jpg "env.py var for testing")
    * in my settings.py:
    * ![setting.py condition for testing](./static/images/readme_images/testing_mode_settings.jpg "setting.py condition for testing")
* Rather than create all my tests in one test.py file, I decided to split them into specific files within each app, naming them as:
    * test_models.py
    * test_urls.py
    * test_forms.py
    * test_views.py

### Tests in ____ app
* In test_urls.py:
   * list all tests
* In test_models.py:
  * list all tests 
  ...
* (All of these tests were successful?)

### Tests in ____ app
*  In test_urls.py:
   * list all tests
* In test_models.py:
  * list all tests
  ...
* All of these tests were successful

...

### Initial Coverage
* After implementing __ successful tests across the models, urls, forms and urls in my apps, I installed Django Coverage.
* Django Coverage installation to viewing html report (following [Code Institute's video](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/dc049b343a9b474f8d75822c5fda1582/5666926980b74689b37a0d5da3cec510/)):
    * pip3 install coverage
    *  {????} set os.environ['TESTING'] = 'yes' in my env.py
    * coverage run --source=cook_ebook manage.py test
    * coverage report
    * coverage html
    * python3 -m http.server 
* Initial coverage report:___%
* screenshot
* From the report I could see that my:
    * anything that needs extra work
* So I revisited my test files in order to cover as many of these missing tests as possible
 
### Further Tests
* Any automated tests you added
  * list them…
  * how much coverage that section then had
  * how much coverage overall now
… 
* List any files you struggled to write automated tests for and list what you did manual tests for:
    * what you were testing (method etc)
    * screenshot

### Manual Testing Other Features (features which you were never going to test automatically e.g. colors on hover and email confirmations)
* Describe feature and what it should do
    * Screenshots of what happens before/after you do something to show the feature works


### Manual JavaScript tests
* Describe feature/functionality
  * screenshots of it working

### Final Coverage 
* After implementing __ successful tests across my models, urls, forms and urls, I installed Django Coverage.
* image of final coverage report
* The areas I was not able to cover with automated testing, I tried to test thoroughly with manual testing (documented in the above sections). 

### PEP8 and Pylint Python Validators
* python file
    * any pylint warnings/errors
    * PEP8 result:

### HTML Validation in Offical W3C Validator (including some likely warnings due to using a templating language)
* list each html template
    * list it's errors/warnings with explanations 
* customised version of django-all_auth's login.html
    * has some Offical W3C Validator errors for using {{ }} and {%  %} syntax, but these are necessary for Django functionality
    * has some Offical W3C Validator errors for missing head element information, but this file extends from base.html which contains the head element
* customised version of django-all_auth's logout.html
    * has some Offical W3C Validator errors for using {{ }} and {%  %} syntax, but these are necessary for Django functionality
    * has some Offical W3C Validator errors for missing head element information, but this file extends from base.html which contains the head element
* customised version of django-all_auth's signup.html
    * has some Offical W3C Validator errors for using {{ }} and {%  %} syntax, but these are necessary for Django functionality
    * has some Offical W3C Validator errors for missing head element information, but this file extends from base.html which contains the head element

### CSS Validation in Offical Jigsaw Validator
* list each css file/end of template script
    * should be no errors or warnings in Offical Jigsaw Validator

### JS Check in JSHint
* list each js file/end of template script
    * should be no errors or warning in JSHint


## Bugs [TO FINISH]
---

### Bugs and Fixes
* Bug: after setting the background-color for the dropdown-menus in the site header to dark grey, when hovering over each item, the background changed to white.
  * Fix: targetting the dropdown-menu hover in base.css and overriding the Bootstrap 5 highlighting, keeping the background-color as dark grey while the links' text was pink on hover.
* Bug: when setting up the header for mobile (small screens) when selecting the Profile/Login icon or expanding the burger icon, their dropdown-menus displayed on the left-hand side of the screen instead of below them.
  * Fix: adding the mobiledropdowncontainer class to both divs containing the dropdown menus and setting their position to relative in base.css, as recommended by [Roy](https://stackoverflow.com/a/35956506) 
* Bug: when I was creating my first instance for the Song model, the slug field would not be set on saving the instance since the slug field had the 'blank=False' constraint.
  * Fix: I replaced the constraint with 'null=True, blank=True' so that the slug could be set by my custom unique_slug_generator method on save.
* Bug: When creating my SongAdmin action methods, in the Songs app admin.py, I had trouble accessing the public field for the instance inorder to check if its value was True or False and to update its value accordingly.
  * Fix: through some trial and error and print statements, I found that the syntax to access the public field's value from the instance was: queryset[0].public.
* Bug: I realised that by using the syntax: queryset[0] I didn't allow for the cases where the selected songs had different values for public/completed/testimonial status and so only the first song's field value was being changed.
  * Fix: I included a for loop in each action method to check the field status for each song in the field set individually. This also resulted in me using the syntax: song.public (to access the field value), song.public = False (to change the field value) and song.save() (to save the change).
* Bug: When manually testing if my header search form worked, the form was only submitted when I hit enter, not when clicking on my search icon.
  * Fix: I had my submit 'button' made from a div element, styled to look like my buttons and with type="submit" and role="button" but the div actually needed to be a button element inorder for it to successfully submit the form.
* Bug: when trying to set the ImageField for my Song model to use my 'placeholder.jpg' as its default image, this only worked when also removing the 'blank=True' option and only for initially creating the Song instance without selecting an image. But without the 'blank=True' it was impossible to clear an existing image from a Song instance, so it would never have the placeholder image set for it.
  * Fix: I added the 'blank=True' back to the ImageField and then where I was overriding the Song model's save method, I added a condition to check if the Song instance didn't have an image and if not, set it to be the 'placeholder.jpg'
* Bug: When creating my select element for filtering searches by Genre, my if statement for setting the 'selected' attribute was not working ocrrectly, even when the Javascript and views logic was working correctly to filter search results.
  * Fix: I removed the {{  }} and ' ' I was using within the 'if selected_genre' statements, which wasn't necessary since these aren't required when already inside template tags (an if statement in this case).
* Bug: When setting up my testimonials template, even though my views and url path were created correctly, I was still receiving a 404 error when trying to open the template in the server. 
  * Fix: I needed to move my testimonials url path above my other urls which contained variables (slugs) since Django searches through the url paths in the order they're written and expects them in order of fewest variables first.
* Bug: When saving custom song forms where the song had capital letters in the name, the unique_slug_generator() method kept being triggered becuase of the way that I was checking if a song's naem had been changed ( not self.slug.split('-')[:-1] == self.name.split(' ') ).
  * Fix: Realising that the the way I was checking the song.name with the slug didn't account for capital letters, I then applied python's .lower() method ( not self.slug.split('-')[:-1] == self.name.lower().split(' ') ) 
* Bug: When saving the custom song form, the formset manager was using the empty instrument form multiple times instead of the clones I had made with the correct values.
  * Fix: Because I was replacing '__ prefix __' with the instrument name rather than a number, the formset manager ignored these created forms, so I had to set up a variable to countr from 0 upwards as I iterated over all the chosen instruments so that I could create their form ids correctly.
* Bug: The formset manager used the empty instrument form as the first of its 'TOTAL_NUM_FORMS' since this hidden empty form was above where I was creating my new instrument forms.
  * Fix: I needed to move the empty form below the container for my created forms so that the formset manager just used the created ones.
* Bug: Trying to use .selected = true/false didn't work when I was trying to change the selected select options for instruments in my custom song form.
  * Fix: I needed to use the .setAttribute() method.
* Bug: When using the .setAttribute() to unselect some instrument options, I used .setAttribute('selected', 'false') but this actually just ll the options to selected and so when it was saved, the form set all the selects to have the final option selected regardless of what was actually chosen.
  * Fix: After discovering that having any 2nd argument for .setAttribute('selected', '2nd_argument') would set the option as selected and that .removeAttribute('selected') should be used, I used the .removeAttribute() method for making sure all unchosen options were not selected, instead.
* Bug: After changing the newly created instruments form's id '__ prefix __' to a number rather than their name, it meant that my method for checking for duplicated instruments and increasing their quantity on one form instead of creating multiple, no longer worked.
  * Fix: I used the list of selected instruments to create a dictionary of instruments as keys with their quantities as their values. Then rather than having an if statement to check if a form already existed for an instrument, I just created the new instrument forms and straight away updated their quannity input value from the disctionary value.
* Bug: When submitting the form in the edit_custom_song template, the formset kept returning as invalid, causing it to keep the old data instead of saving any changes to the instruments. On inspecting the invalid formsets in the terminal, I could see that some of the instruments had error notes saying that they were a requireed field even though they contained the right data.
  * Fix: Setting the value of the formset management div with id="id_song_instruments-INITIAL_FORMS" to zero, since the whole formset was being recreated anytime the user made any changes to the formset, so it wasn't necessary to be tracking the number of initial forms.
* Bug: Whenever a success message was being displayed, an overview of the tracklist was also being displayed, even if the user was just logging in or saving a custom song design.
  * Fix: I set an if statement in the toast_success snippet to only display the tracklist overview if a session variable 'updating_tracklist' had the value 'true'. Then in the AddToTracklist and RemoveFromTracklist views, I set the 'updating_tracklist' session variable to 'true' and in the contexts.py file I stored the session variable's value in a local 'updating_tracklist' variable. I then set a show_tracklist_overview_in_message variable to have the value from the 'updating_tracklist' variable and then set 'updating_tracklist' to 'false' and pass the 'show_tracklist_overview_in_message' into the context dictionary.
* Bug: When I added the url path to my delete button in the edit_custom_song template, everytime I tried to access the edit page, I got an error saying that there was no reverse for 'delete_confirmation'.
  * Fix: I realised that I was not passing the actual song instance into the edit_custom_song template, so I added this to the context in the EditCustomSong() view get method.
* Bug: My method for checking for the 'updating_tracklist' session variable and showing or not showing the rtacklist overview with any success messages appeared to not be working. After adding one item to the tracklist it would then always show the rtacklist overview in success messages, regardless of what they were for.
  * Fix: In contexts.py when I was changing the 'updating_tracklist' to 'false' this was actually only changing the value of the local variable, not updating the session variable, so I changed: updating_tracklist = 'false' to be: request.session['updating_tracklist'] = 'false'. After making this change it was also clear that the 'show_tracklist_overview_in_message' local variable was redundant, so I just used the local 'updating_tracklist' instead.
* Bug: 
  * Fix:


### Unfixed Bugs
* Should be: No known unfixed bugs (other than warnings/errors explained in code validation section)


## Deployment [TO FINISH]
---

### Early Deployment to Heroku (adjust for this project)
* First I created the cook-ebook app on Heroku
* Then I added my Heroku Postgres database in Heroku's Resources -> Add Ons
* I created an env.py file in my root directory and made sure that it was listed in my .gitignore so that it would never be commited to GitHub
* I copied the link to my Heroku database from the Heroku Config Variable and pasted it into my env.py file
* In my env.py file I created variables for my DATABASE_URL and my SECRET_KEY
* I gave my SECRET_KEY a value and created a Heroku Config Variable for this 
* I then changed my default database to use dj_database_url and DATABASE_URL
* In my settings.py file I set my Heroku app as a localhost in my ALLOWED_HOSTS variable
* After installing Cloudinary, I created a 'DISABLE_COLLECTSATIC' Config Variable in Heroku with a value of '1', since I didn't have any staticfiles at that time
* I then created a Procfile for my app
* Set auto deploys

### Final Deployment to Heroku
* 

### Deployed site link
* link


## Credits [TO FINISH]
---

### Helpful Resources
* [dbdiagram.io](https://dbdiagram.io/home) for creating my initial and final database schema designs.
* [GeeksforGeeks' solution](https://www.geeksforgeeks.org/how-to-remove-arrow-in-dropdown-in-bootstrap/) for how to remove the arrow from the Bootstrap dropdowns.
* [cssgradient's online tool](https://cssgradient.io/) used to help visualise the homepage background gradient.
* [Typewolf](https://www.typewolf.com/google-fonts) for finding the best Google fonts for this project.
* [Code Institute's 'friendly_name' models field idea](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/f6c3de32aa152b98da174daba13412388258b9b8/products/models.py) for how to have a programamtic and displayed version of my Genre and Instrument instances. This was useful because the search functionality required the Genre and Instrument names to be written programatically (with no uppercases or spaces) but it was better for the UXD for the Genre and Instrument names to contain uppercases and spaces when displayed to users.
* [Code Institute's idea for creating order numbers by overriding the default save method](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/f6c3de32aa152b98da174daba13412388258b9b8/checkout/models.py) for how to call my unique_slug_generator method to make sure that all Song instances have a slug, which is used in urls as a unique identifier to avoid exposing mydatabase's primary keys.
* [Tom's solution on Stackoverflow](https://stackoverflow.com/a/42426801) for how to use Django's PositiveIntegerField with minimum and maximum value constraints.
* [Fagan Media's page](https://www.faganmedia.com/support/disable-download-button-for-html5-audio-and-video-player) for how to disable the 'download' option from the audio element.
* [Point Clear Media's page](https://pointclearmedia.com/2020/08/27/css-styling-the-audio-element/) for how to target parts of the audio element to style it. 
* [W3School's page](https://www.w3schools.com/howto/howto_js_get_url.asp) for how to get the current window's url with javascript.
* [Metring's page](https://ricardometring.com/getting-the-value-of-a-select-in-javascript) for how to get the value of a selected select option with javascript.
* [Code Institute's idea for setting a background image on the body element and then using an overlay to cover it on other pages](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/933797d5e14d6c3f072df31adf0ca6f938d02218/static/css/base.css) for why I set a background image on my body element, which is visible on the landing page and on pages where I just wanted my dark grey background I craeted a custom overlay. The reason I applied this to the body for all pages instead of just the landing page is that the body background image loads quicker than other content on the page, so if a page takes a moment to load fully, the site's landing page image is visible in the background instead of a plain white background.
* CodingEntrepreneurs's videos on [get absolute url](https://www.youtube.com/watch?v=b42B-xli-vQ&list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL&index=47) and [Django URLs Reverse](https://www.youtube.com/watch?v=rm2YTMc2s10&list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL&index=46) for how to implement the get_absolute_url method on my Song model.
* Django Adventure's page on [How to create file download links in Django?](https://djangoadventures.com/how-to-create-file-download-links-in-django/) for the last part of how I wrote the logic for downloading a song to a user's device in my DownloadSong view. Most of the view's functionality is custom code but the overall logic was heavily influenced by Django Adventure's page.
* [Banjer's solution on Stackoverflow](https://stackoverflow.com/a/10290401) for how to use Django's template tags to truncate values by a number of characters. I used this for my testimonials page so that long testimonials text wouldn't cause the layout to break or become mishappen.
* [im_brian_d's solution on Stackoverflow](https://stackoverflow.com/a/26133651) for how to stop Bootstrap carousels from auto changing slides, using the data-bs-interval="false" attribute on the carousel itself.
* [russ_ferri's solution on Stackoverflow](https://stackoverflow.com/a/11552460) and [w3schools' page on object-fit](https://www.w3schools.com/csS/css3_object-fit.asp) for how to correctly position and fit images centrally with css rules. I used this for the testimonial carousel images so that they always filled the container without being streched, but also were cetralised.  
* [Abdul Niyas P M's solution on Stackoverflow](https://stackoverflow.com/a/56645085) for how to change the default django form labels for form fields in forms.py.  
* [ClarkTheCoder's solution on Stackoverflow](https://stackoverflow.com/a/51351682) for how to add placeholder text to Textarea fields using django widgets in forms.py.  
* [Daniel Roseman's solution on Stackoverflow](https://stackoverflow.com/a/55237245) for using values_list() method to get a queryset for Genre with each value by its display_name for using in the form dropdown.  
* [Ishita Kabra's solution on Stackoverflow](https://stackoverflow.com/a/68891518) for how to add css style rules to the file-upload-button, which I used to style my image upload button in my Design Custom Song form.  
* [Eliakin Costa's solution on Stackoverflow](https://stackoverflow.com/a/59364708) for how to apply an 'empty_label' attribute to django's ModelChoiceFields, which I used for my project_type and genre fields.  
* [TLindig's solution on Stackoverflow](https://stackoverflow.com/a/14438954) for a way to get all of the unique values in a JavScript array, by creaing a new Set() from it, which I used for my Design Custom Song Form, in order to find the number of unqiue instruments the user chooses, in my updateInstrumentFormsets() function.
* [Felix Kling's solution on Stackoverflow](https://stackoverflow.com/a/5882802) for a way to insert my additional instrument dropdowns above the Add An Instrument button in my addINstrument() function for my Design Custom Song Form.
* [Mahesh Velaga's solution on Stackoverflow](https://stackoverflow.com/a/4435190) for how to get my displayed price to show only to 2 decimal places after using parseFloat(), with toFixed(2), in my Design Custom Song Form.
* [GeeksforGeeks' page](https://www.geeksforgeeks.org/how-to-check-an-element-with-specific-id-exists-using-javascript/) for checking if an instrument formset id already exists in my updateInstrumentFormsets() function for my Design Custom Song Form.
* [EDUCBA's page](https://www.educba.com/javascript-disable-button/) on how to disable buttons with JavaScript, which I used in my checkReviewSessionButtons() function for my Design Custom Song Form.
* [JavaScript Tutorial's page](https://www.javascripttutorial.net/dom/manipulating/clone-an-element/) on how to clone an element and all its children with JavaScript, which I used in my Design Custom Song Form.
* [Willem Van Onsem's solution on Stackoverflow](https://stackoverflow.com/a/60871659) for how to apply the 'login_required' decorator to a url path, which I used to ensure only logged in users can access the Design Custom Form.
* [Delft Stack's solution](https://www.delftstack.com/howto/javascript/javascript-loop-through-dictionary/) for how to handle iterating through a dictionary's keys and value in a for loop, which I used in my updateInstrumentFormsets() function for my design_custom_song form.
* [Kenny Shen's solution on Stackoverflow](https://stackoverflow.com/a/13016982) for how to use the post_save() signal, which I used my SongInstrument model inorder to trigger the price calculation for custom songs.
* [JP Silvashy's solution on Stackoverflow](https://stackoverflow.com/a/2003831) for how to use .shift() in javascript in order to get the first item from an array whilst also removing it from the list. I used this in the Javascript for my edit custom song template when pre-populating each instrument select with the existing instruments.
* [linehammer's solution](https://dev.to/mmeurer00/location-reload-a55) for how to reload my checkout page without charging the user if the payment fails for any reason. Used in my submit event listener on the form in my stripe_elements.js.
* [Python docs - uuid](https://docs.python.org/3/library/uuid.html) for how to use UUID objects, which I used to generate my order_number for my Order model.


### Content
* Fonts:
  * Google Font's [BioRhyme](https://fonts.google.com/specimen/BioRhyme) for the logo font and headings.
  * Google Font's [Fira Sans](https://fonts.google.com/specimen/Fira+Sans) for the rest of the site's text content.

### Code
* (FINISH ... installed django extensions if any)
* Expandable navbar made with [Bootstrap 5 navbars](https://getbootstrap.com/docs/5.0/components/navbar/#external-content)
* Dropdown menus made with [Bootstrap 5 dropdowns](https://getbootstrap.com/docs/5.0/components/dropdowns/)
* Email Subscription form created with [Mailchimp's](https://mailchimp.com/en-gb/) Embedded Form Builder
* My Song modle's unique_slug_generator method uses my own [random_slug method from my Cook eBook project](https://github.com/mountaincharlie/project-four-cook-ebook/blob/main/cook_ebook/models.py) with the small addition of using the name of the Song in the slug to further reduce the chance of duplicate slugs
* I used [W3School's Audio Element page](https://www.w3schools.com/html/html5_audio.asp) to find the code for setting up the audio element with controls
* In order to create the 'sort by' dropdown selector, I followed and adapted the logic implemented in Code Institue's walkthrough project for; the select element and Javascript in their [products template](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/f6c3de32aa152b98da174daba13412388258b9b8/products/templates/products/products.html) and the view function logic in their [all_products view function](https://github.com/mountaincharlie/e-commerce-walkthrough-project/blob/main/products/views.py)
* My JavaScript for implementing my Genres select in the All Pre-made Songs browsing page, was based on and adapted from the logic for the Sort Select described above, but the html and python in the views.py was custom made for this project.
* The views logic for my 'like' button on the song_details pages was adapted from my [RecipeChefsKissView view](https://github.com/mountaincharlie/project-four-cook-ebook/blob/main/cook_ebook/views.py) in my Cook eBook project.
* Testimonials Carousel made with [Bootstrap 5 carousels](https://getbootstrap.com/docs/5.0/components/carousel/) with controls, indicators and captions. I adapted this code quite a bit to fit how I was creating the slides with a for loop and for how I styled it to fit with the rest of the site.
* In order to keep the user on their current page when adding/removing items to their Tracklist I used [Code Institute's method](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/933797d5e14d6c3f072df31adf0ca6f938d02218/products/templates/products/product_detail.html) of having a hidden input with; name="redirect_url" value="{{ request.path }}, and then getting the redirect_url in the View in order to redirect the user to the correct url after adding/removing a song to their Tracklist. I used this on my song_details pages as well as when browsing songs.
* Stripe's [Setup Stripe.js and Submit the payment to Stripe](https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements) sections used for setting up the stripe and elements vars, styling the card element in stripe_elements.js.
* [Stripe.js](https://stripe.com/docs/payments/accept-card-payments?platform=web&ui=elements) used for creating and mounting the card element and form submit event
listner in stripe_elements.js.
* [Code Institute's walkthrough](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/933797d5e14d6c3f072df31adf0ca6f938d02218/checkout/static/checkout/js/stripe_elements.js) used for the 'change' event listener and form 'submit' event listener logic which I adapted for this project, in stripe_elements.js.
* [Code Institute's walkthrough](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/933797d5e14d6c3f072df31adf0ca6f938d02218/checkout/webhooks.py) used for the webhook function logic adapted for this project in webhooks.py.
* The logic from the above credit is also originally from Stripe's documentation for [handling webhooks](https://stripe.com/docs/payments/handling-payment-events#create-webhook).
* [Code Institute's walkthrough](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/933797d5e14d6c3f072df31adf0ca6f938d02218/checkout/webhook_handler.py) used for the StripeWH_Handler logic adapted for this project in webhook_handler.py.
* [Code Institute's walkthrough](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/933797d5e14d6c3f072df31adf0ca6f938d02218/checkout/views.py) used when creating my checkout app view classes and functions - logic adapted for this project, from Code Institute's walkthrough.
* Using [auto payment menthods in python from the Stripe docs](https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements) to create the PaymentIntent in checkout/views.py CheckoutView.
* [Code Institute's walkthrough](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/933797d5e14d6c3f072df31adf0ca6f938d02218/checkout/models.py) for the structure that I based my Order model from, adapted for this project.

### Media
* Images:
  * Homepage background - by [moutaincharlie](https://github.com/mountaincharlie)
  * For Finding My Place song - by [moutaincharlie](https://github.com/mountaincharlie)
  * For Someplace song - by [Jérôme Prax on Unsplash](https://unsplash.com/photos/jLZWzT_kdTI?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)
  * 
* Icons:
  * Font Awesome's …
  * Favicon made Font Awesome's …


## Future Features [TO FINISH]
---
Ideas that could be used to expand the site's functionality. 

### AdOns
* 