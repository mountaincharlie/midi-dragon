// jshint esversion: 6

// JS for handling the instruments formsets, number of review sessions and the on-screen price calculation
 
// credit for techniques you used in your P4 project?

// ---- GLOBAL VARS

// getting the 'song_instruments-TOTAL_FORMS' div so that I can update this number in the updateInstrumentFormsets(function)
let totalSelectedInstruments = document.getElementById('id_song_instruments-TOTAL_FORMS');

// gets the + and - buttons for review sessions section
let addReviewSessionButton = document.getElementById('add-num-of-reviews');
let subtractReviewSessionButton = document.getElementById('subtract-num-of-reviews');

// gets the max-num-review-sessions variable passed from view context
let maxNumReviewSessions = document.getElementById('max-num-review-sessions').innerText;

// gets the additional-instrument-price variable passed from view context
let additionalInstrumentPrice = document.getElementById('additional-instrument-price').innerText;

// gets the additional-review-session-price variable passed from view context
let additionalReviewSessionPrice = document.getElementById('additional-review-session-price').innerText;

// gets the num-of-reviews-container
let numOfReviewsContainer = document.getElementById('num-of-reviews-container');

// gets the form input for id_num_of_reviews
let numOfReviewsInput = document.getElementById('id_num_of_reviews');

// gets the select for choosing project type
let projectTypeDropdown = document.getElementById('id_project_type');

// gets the display-price-container
let displayPriceContainer = document.getElementById('display-price-container');

// gets the add-song-instrument-container
let addInstrumentButtonContainer = document.getElementById('add-song-instrument-container');

// gets the additional-instruments-container
let additionalInstrumentsContainer = document.getElementById('additional-instruments-container');

// gets the additional-instruments-select-container by class from #hidden-instrument-elements
let additionalInstrumentsSelectContainer = document.getElementById('hidden-instrument-elements').getElementsByClassName('additional-instruments-select-container')[0];

// gets all the instruments-select elements
let instrumentsSelects = document.getElementsByClassName('instruments-select');

// gets div_id_use_as_testimonial
let useAsTestimonialCheckboxContainer = document.getElementById('div_id_use_as_testimonial');
            
// gets the div_id_use_as_testimonial checkbox
let useAsTestimonialCheckbox = useAsTestimonialCheckboxContainer.childNodes[1];

// gets the instrument-formsets-container 
let instrumentFormsetContainer = document.getElementById('instrument-formsets-container');

// gets the empty formset new-instrument-form
let newEmptyInstrumentForm = document.getElementById('new-instrument-form')

// gets the included-instruments-container
let includedInstrumentsContainer = document.getElementById('included-instruments-container');


// ---- FUNCTION CALLS AND EVENT LISTENERS ON DOM LOAD
document.addEventListener('DOMContentLoaded', function(){

    // change event listener on project_type
    projectTypeDropdown.addEventListener('change', projectTypeChosen);

    // calling the projectTypeChosen function if the dropdown value is already not the reset value (e.g. if in Edit mode)
    if (projectTypeDropdown.value != ''){
        // calls projectTypeChosen function - IF it resets insrtuments => FIX
        projectTypeChosen(projectTypeDropdown);
        console.log(projectTypeDropdown)
        // console.log(projectTypeDropdown.options.selectedIndex)


        // let existingProjectType = projectTypeDropdown[projectTypeDropdown.options.selectedIndex];
        // let newProjectType = projectTypeDropdown[parseInt(projectTypeDropdown.options.selectedIndex)+1];

        // existingProjectType.removeAttribute('selected');
        // newProjectType.setAttribute('selected', 'true');
        // newProjectType.removeAttribute('selected');
        // existingProjectType.setAttribute('selected', 'true');
    
        // console.log(projectTypeDropdown[projectTypeDropdown.options.selectedIndex].setAttribute('selected', 'true'))
    };


    // adding event listener to + review session button
    addReviewSessionButton.addEventListener('click', addReviewSession);

    // adding event listener to - review session button
    subtractReviewSessionButton.addEventListener('click', subtractReviewSession);

    // click event listener on the Add instrument buttons
    addInstrumentButtonContainer.childNodes[1].addEventListener('click', addInstrument);

    // change event listener on the instrument dropdown
    // when any value is chosen => checks the hidden formset management [a formset management update function used by both the dropdown and the delete button] and compares all of the displayed dropdown values with the existing formsets, for each displayed instrument, if there isnt a formset for it, it creates one, if there is then it updates the quantity and if there is a formset existing for an instrument that isnt displayed anymore then it deletes that formset


    // click event listener on the Delete instrument buttons
    // (only available on additional instruments)
    // when clicked => removes its assocaited instrument dropdown (and the delete button itself) and then checks the hidden formset management [a formset management update function used by both the dropdown and the delete button] and compares all of the displayed dropdown values with the existing formsets, for each displayed instrument, if there isnt a formset for it, it creates one, if there is then it updates the quantity and if there is a formset existing for an instrument that isnt displayed anymore then it deletes that formset
            
    // event listener on use-as-testimonial checkbox
    useAsTestimonialCheckbox.addEventListener('change', toggleTestimonialTextContainer)

    // change event listener on bpm input to change value if its outside the allowed range => prevents the validation breaking the form
    let bpmInput = document.getElementById('id_bpm')
    bpmInput.addEventListener('change', validateBpmInput)

    // style changes for the 'currently' image section (in 'edit_custom_song')
    if (document.getElementById('image-clear_id')){
        styleCurrentImageSection();
    }

    // calling toggleTestimonialTextContainer() to check if its already ticked
    toggleTestimonialTextContainer();

});


/**
 * @name projectTypeChosen
 * @description 
*/
// if set to nothing/empty => add d-none class to all the buttons and selects and remove d-none class from the 2 notes about needing to choose a project_type. Also resets the displayed price and all of the background formsets [just reload page? - TRY]
// if #id_project_type innerText == 'Mini'/'Regular'/'Pro' => un-hide the note about changing the project_type will reset the instrument/reviews/price sections, and apply d-none class to the 2 notes about choosing projeect_type, display min_num_reviews and the +/- buttons with the minus button DISABLED, remove d-none from the included/additional instruments subheadings and hr, insert into #included-instruments-container the min_num_instruments amount of instrument dropdowns and remove the d-none from the Add Instrument button in the additional instruments section. Also sets the displayed price as the min_price (from the project_type)
function projectTypeChosen(ev){
    // checking if the function is being triggered by the change event listener
    if (ev.type == 'change'){
        ev.preventDefault();
        srcElement = ev.srcElement;
        console.log('from event listener')
        // clearing instrumentFormsetContainer's innerHTML since the project type has changed (but not in edit mode)
        instrumentFormsetContainer.innerHTML = '';
    } else {
        // TRIGGER THIS PRE-POP FUNCTION - PASSING srcElement in?
        srcElement = ev;
        console.log('ev', ev)
        console.log('type already chosen (edit mode)')
    };

    // getting the index of the selected project type
    
    let selectedProjectTypeIndex = srcElement.options.selectedIndex;
    console.log('selectedProjectTypeIndex', selectedProjectTypeIndex)
    let selectedProjectTypeText = srcElement[selectedProjectTypeIndex].innerText;
    // let selectedProjectTypeIndex = ev.srcElement.options.selectedIndex;
    // let selectedProjectTypeText = ev.srcElement[selectedProjectTypeIndex].innerText;

    // -------- getting all the elements which need d-none adding/removing

    // gets all of the select-a-project-msg notes
    let selectAProjectMessages = document.getElementsByClassName('select-a-project-msg');
            
    // gets the changing-project-type-msg note
    let changingProjectTypeMsg = document.getElementById('changing-project-type-msg');

    // gets the price-calculation-note note
    let priceCalulationNote = document.getElementById('price-calculation-note');
            
    // gets the included-instruments-subheading heading
    let includedInstrumentsSubheading = document.getElementById('included-instruments-subheading');

    // gets the additional-instruments-subheading heading
    let additionalInstrumentsSubheading = document.getElementById('additional-instruments-subheading');

    // gets the visible-instruments-dropdown hr
    let visibleInstrumentsDropdownHr = document.getElementById('visible-instruments-dropdown').getElementsByClassName('hr-90-light')[0];

    // gets the review-sessions-buttons
    let reviewSessionsButtons = document.getElementById('review-sessions-buttons');

    // gets project-type-duration-range-container
    let projectTypeDurationRangeContainer = document.getElementById('project-type-duration-range-container');

    // gets the project-type-duration-range-note
    let projectTypeDurationRangeNote = document.getElementById('project-type-duration-range-note');

    // resetting totalForms value
    totalSelectedInstruments.value = 0;


    // if ev.srcElement.options.selectedIndex = 0 => reset
    if (selectedProjectTypeIndex == 0){
        // ------ handling the d-none classes

        // rmv d-none from select-a-project-msgs
        for (const message of selectAProjectMessages){
            message.classList.remove('d-none');
        }
        // add d-none to changing-project-type-msg
        changingProjectTypeMsg.classList.add('d-none');
        // add d-none to included-instruments-subheading
        includedInstrumentsSubheading.classList.add('d-none');
        // add d-none to additional-instruments-subheading
        additionalInstrumentsSubheading.classList.add('d-none');
        // add d-none to the visible-instruments-dropdown hr
        visibleInstrumentsDropdownHr.classList.add('d-none');
        // add d-none to the num-of-reviews-container
        numOfReviewsContainer.classList.add('d-none');
        // add d-none to the review-sessions-buttons
        reviewSessionsButtons.classList.add('d-none');
        // add d-none to the price-calculation-note
        priceCalulationNote.classList.add('d-none');
        // add d-none to the project-type-duration-range-container
        projectTypeDurationRangeContainer.classList.add('d-none');
        // resetting the projectTypeDurationRangeNote innerText
        projectTypeDurationRangeNote.innerText = '';

        // setting blank num of reviews for displayed and the input
        numOfReviewsContainer.innerText = '';
        numOfReviewsInput.setAttribute('value', 'N/A')

        // ------ inserting price
        displayPriceContainer.innerText = '...';


        // ------ clearning the included instruments container
        includedInstrumentsContainer.innerHTML = '';
                
        // ------ clearing the additional instruments container
        additionalInstrumentsContainer.innerHTML = '';

    }
    // if any other project type selected
    else {
        // ------ handling the d-none classes

        // add d-none to select-a-project-msgs
        for (const message of selectAProjectMessages){
            message.classList.add('d-none');
        }
        // rmv d-none from changing-project-type-msg
        changingProjectTypeMsg.classList.remove('d-none');
        // rmv d-none from included-instruments-subheading
        includedInstrumentsSubheading.classList.remove('d-none');
        // rmv d-none from additional-instruments-subheading
        additionalInstrumentsSubheading.classList.remove('d-none');
        // rmv d-none from the visible-instruments-dropdown hr
        visibleInstrumentsDropdownHr.classList.remove('d-none');
        // rmv d-none from the num-of-reviews-container
        numOfReviewsContainer.classList.remove('d-none');
        // rmv d-none from the review-sessions-buttons
        reviewSessionsButtons.classList.remove('d-none');
        // rmv d-none from the price-calculation-note
        priceCalulationNote.classList.remove('d-none');

        // gets duration range for p type
        let projectDurationRange = document.getElementById(`song-length-range-${selectedProjectTypeText}`).innerText;

        // inserting the duration range into project-type-duration-range-note
        projectTypeDurationRangeNote.innerText = projectDurationRange;

        // rmv d-none from the project-type-duration-range-container
        projectTypeDurationRangeContainer.classList.remove('d-none');

        // ------ inserting price
        let projectMinPrice = document.getElementById(`min-price-${selectedProjectTypeText}`).innerText;

        displayPriceContainer.innerText = `£ ${projectMinPrice}`;


        // ------ handling the number of review sessions
        let projectMinNumOfReviews = document.getElementById(`num-included-reviews-${selectedProjectTypeText}`).innerText;

        // if the event type is not 'change' => edit => dont override numOfReviewsContainer value
        // compare existing review sessions with project type minimum and call addReviewSession() for each extra review session
        if (ev.type != 'change'){
        
            // gets num-of-existing-reviews-container innerText
            let existingNumReviewSessions = document.getElementById('num-of-existing-reviews-container').innerText;
            console.log('existingNumReviewSessions', parseInt(existingNumReviewSessions))

            // sets the existing review sessions value
            numOfReviewsContainer.innerText = projectMinNumOfReviews;
            numOfReviewsInput.setAttribute('value', parseInt(projectMinNumOfReviews));

            if(parseInt(existingNumReviewSessions) > parseInt(projectMinNumOfReviews)){
                // console.log('--------MORE EXISTING REVIEWS')
                let numAdditionalReviews = parseInt(existingNumReviewSessions) - parseInt(projectMinNumOfReviews)

                for(let i = 0; i < numAdditionalReviews; i++){
                    // console.log('--------CALLING addReviewSession')
                    // calls addReviewSession()
                    addReviewSession();
                };
            };

        } else {
            numOfReviewsContainer.innerText = projectMinNumOfReviews;
            numOfReviewsInput.setAttribute('value', parseInt(projectMinNumOfReviews));
        };

        
        // calling the check buttons function
        checkReviewSessionButtons(numOfReviewsContainer.innerText, projectMinNumOfReviews, maxNumReviewSessions);
    
                
        // ------ clearing the included instruments container
        includedInstrumentsContainer.innerHTML = '';

        // gets the number of included instruments
        let projectNumOfInstruments = document.getElementById(`num-included-instruments-${selectedProjectTypeText}`).innerText;
        // console.log('projectNumOfInstruments', projectNumOfInstruments);

        // ------ inserting copies of the instrument dropdowns into the included instrumnets container
        for (var i = 0; i < projectNumOfInstruments; i++){
            // creates cloneNode of the hidden instruments-select
            let newInstrumentSelect = document.getElementById('hidden-instrument-elements').getElementsByClassName('instruments-select')[0].cloneNode(true);
            // appends it as a child
            includedInstrumentsContainer.appendChild(newInstrumentSelect);
        }

        // ------ clearing the additional instruments container
        additionalInstrumentsContainer.innerHTML = '';

        // clones the addInstrumentButton button
        addInstrumentButtonContainer.cloneNode(true);
        // inserts the button into the additionalInstrumentsContainer (ALWAYS last child)
        additionalInstrumentsContainer.appendChild(addInstrumentButtonContainer);

        // gets all the instrumentsSelects elements

        // applies the change event listener to all the instrumentsSelects
        for (let instrument of instrumentsSelects){
            instrument.addEventListener('change', updateInstrumentFormsets);
        }

    };

    // for edit mode => populating the instruments-select elements
    if (ev.type != 'change'){
        console.log('pre-popping for existing instruments')
        console.log('instrumentsSelects',instrumentsSelects[1])
        // NEED TO manually pre-pop the displayed inputs
        // gets the hidden existing-instrument
        let existingInstruments = document.getElementsByClassName('existing-instrument')

        // setting up totalNumPrepopSelects var and instrumentNames list
        let totalNumPrepopSelects = 0;
        let instrumentNames = [];
        for (let i = 0; i < existingInstruments.length; i++){
            let instrumentQuantity = existingInstruments[i].innerText.split('-')[0]
            let instrumentName = existingInstruments[i].innerText.split('-')[1]
            console.log('existingInstrument quantity:', instrumentQuantity)
            console.log('existingInstrument name:', instrumentName)

            totalNumPrepopSelects = parseInt(totalNumPrepopSelects) + parseInt(instrumentQuantity);
            for (let i = 0; i < instrumentQuantity; i++){
                instrumentNames.push(instrumentName);
            }
            
        }
        console.log('totalNumPrepopSelects:', totalNumPrepopSelects)
        console.log('instrumentNames:', instrumentNames)
        
        // uses the instrumentsSelects var  we just want the first totalNumPrepopSelects
        // console.log('instrumentsSelects:', instrumentsSelects)

        // gets the number of instruments included in the project type 
        let projectNumOfInstruments = document.getElementById(`num-included-instruments-${selectedProjectTypeText}`).innerText;

        // checking how many additional selects are required 
        let numAdditionalSelects = parseInt(totalNumPrepopSelects) - parseInt(projectNumOfInstruments);
        console.log('numAdditionalSelects:', numAdditionalSelects)


        // included selects are the number of projectNumOfInstruments if additional are required
        if (numAdditionalSelects > 0){

            // for numAdditionalSelects calls the addInstrument
            for(let i = 0; i < numAdditionalSelects; i++){
                // calls addInstrument()
                addInstrument();
            };

            // calling prepopulateExistingInstrumentSelects() for all the visible selects
            prepopulateExistingInstrumentSelects(instrumentNames, instrumentsSelects.length);
        }
        // else included selects are just the totalNumPrepopSelects
        else {
            let numIncludedSelects = parseInt(totalNumPrepopSelects);

            prepopulateExistingInstrumentSelects(instrumentNames, numIncludedSelects);
        }

        // applies the change event listener to all the instrumentsSelects
        for (let instrument of instrumentsSelects){
            instrument.addEventListener('change', updateInstrumentFormsets);
        }

        // gets id_song_instruments-INITIAL_FORMS to set the vaule to 0
        let numSongInstrumentsInitialForms = document.getElementById('id_song_instruments-INITIAL_FORMS')
        numSongInstrumentsInitialForms.setAttribute('value', 0)

        // calling the updateInstrumentFormsets function
        updateInstrumentFormsets()
    };
};


// prepopulateExistingInstrumentSelects
/**
 * @name prepopulateExistingInstrumentSelects
 * @description 
*/
function prepopulateExistingInstrumentSelects(instrumentNames, counter){

    for (let i = 0; i < counter; i++){
        // goes through the selects and sets the instrument from instrumentNames as the selected option and then pops that value from the list (needs to de-select all other options)

        // removes first instrumentNames list item and stores in instrument
        let instrument = instrumentNames.shift();
        console.log(instrument)

        let currentSelect = instrumentsSelects[i];

        // loops through all options and selects the right one
        for (let i = 0; i < currentSelect.length; i++){
            let optionValue = currentSelect[i].getAttribute('value');
            // console.log('optionValue', optionValue)
            currentSelect[i].removeAttribute('selected');

            if (optionValue == instrument){
                currentSelect[i].setAttribute('selected', true);
            }
        }
    }
}


// updateInstrumentFormsets
/**
 * @name updateInstrumentFormsets
 * @description 
*/
function updateInstrumentFormsets(ev){
    if (ev){
        ev.preventDefault();
    }
    // clearing instrumentFormsetContainer's innerHTML
    instrumentFormsetContainer.innerHTML = '';

    // creates empty array to append all valid instrument selections
    let currentInstrumentSelection = [];

    // adds all selected instruments to currentInstrumentSelection
    for(let selectElement of instrumentsSelects){
        let selectValue = selectElement[selectElement.options.selectedIndex].value;
        if (selectValue != 'reset'){
            currentInstrumentSelection.push(selectValue);
        }
    }

    let numUniqueInstrumentSelection = new Set(currentInstrumentSelection).size;

    // create dictionary
    let currentInstrumentSelectionDict = {};
    for (let instrument of currentInstrumentSelection){

        if (instrument in currentInstrumentSelectionDict){
            // adds 1 to the value
            currentInstrumentSelectionDict[instrument] = currentInstrumentSelectionDict[instrument] + 1;
        } else {
            // creates the key with value = 1
            currentInstrumentSelectionDict[instrument] = 1;
        }
    }
    console.log('INSTRUMENT DICT', currentInstrumentSelectionDict);

    // ---- create formsets for all unique and update quantity for duplicates [CREDIT - based on some logic i implemented in my P4 project]

    // resetting the counter for the instrument ids
    let instrumentId = 0;

    // for loop iterating through the dictionary of instruments and their quantities
    for (const [instrument, quantity] of Object.entries(currentInstrumentSelectionDict)){

        let instrumentFormsetId = `instrument-form-${instrumentId}`; 
                
        // gets a clone of the hidden new-instrument-form
        const clonedNewEmptyInstrumentForm = newEmptyInstrumentForm.cloneNode(true);
            // let newEmptyInstrumentForm = document.getElementById('new-instrument-form').cloneNode(true);
            // applies its id
            clonedNewEmptyInstrumentForm.setAttribute('id', instrumentFormsetId);
            // appends it to the instrumentFormsetContainer as a child
            instrumentFormsetContainer.appendChild(clonedNewEmptyInstrumentForm);

            // Uses a regular expression to change __prefix__ to the instrument name so that the name and id for each form input will be related and unique as more are added
            const regexp = new RegExp('__prefix__', 'g');clonedNewEmptyInstrumentForm.innerHTML = clonedNewEmptyInstrumentForm.innerHTML.replace(regexp, instrumentId);

            // gets the select and sets its value
            let newEmptyInstrumentFormSelect = document.getElementById(`id_song_instruments-${instrumentId}-instrument`);
                    
            // loops through all options and selects the right one
            for (i = 0; i < newEmptyInstrumentFormSelect.length; i++){
                let optionInnerText = newEmptyInstrumentFormSelect[i].innerText;
                newEmptyInstrumentFormSelect[i].removeAttribute('selected');

                if (optionInnerText == instrument){
                    newEmptyInstrumentFormSelect[i].setAttribute('selected', true);
                }
            }
            // checking the correct option is now selected
            // console.log(newEmptyInstrumentFormSelect.options[newEmptyInstrumentFormSelect.selectedIndex]);

            // getting the quantity input
            let existingInstrumentFormQuantityInput = document.getElementById(`id_song_instruments-${instrumentId}-quantity`);

            // sets quantity from the dict value
            existingInstrumentFormQuantityInput.setAttribute('value', quantity);
                    
                
        // adds 1 to counter for setting the instruments id number
        instrumentId = parseInt(instrumentId) + 1
    }
    // update value of totalSelectedInstruments by getting the number of unique values
    totalSelectedInstruments.setAttribute('value', numUniqueInstrumentSelection);
    // checking total forms value is updated
    // console.log('totalSelectedInstruments', totalSelectedInstruments);
};



/**
 * @name addInstrument
 * @description 
*/
function addInstrument(ev){
    if (ev){
        ev.preventDefault();
    }
    // creates cloneNode of the additional-instruments-select-container
    let newInstrumentSelect = additionalInstrumentsSelectContainer.cloneNode(true);

    // appends it as a child
    additionalInstrumentsContainer.insertBefore(newInstrumentSelect, addInstrumentButtonContainer);

    // gets all of the delete-instrument-select-button buttons
    let deleteInstrumentsSelectButtons = document.getElementsByClassName('delete-instrument-select-button');

    // applies a click event listner to them all
    for (let button of deleteInstrumentsSelectButtons){
        button.addEventListener('click', deleteAdditionalInstrument);
    }

    // applies the change event listener to all the instrumentsSelects
    for (let instrument of instrumentsSelects){
        instrument.addEventListener('change', updateInstrumentFormsets);
    }

    // increases the displayed price
    displayPriceContainer.innerText = `£ ${(parseFloat(displayPriceContainer.innerText.replace('£', '')) + parseFloat(additionalInstrumentPrice)).toFixed(2)}`;
};


/**
 * @name deleteAdditionalInstrument
 * @description 
*/
function deleteAdditionalInstrument(ev){
    if (ev){
        ev.preventDefault();
    }
    // removes its parent ('additional-instruments-select-container')
    ev.srcElement.parentElement.remove();

    // decreases the displayed price
    displayPriceContainer.innerText = `£ ${(parseFloat(displayPriceContainer.innerText.replace('£', '')) - parseFloat(additionalInstrumentPrice)).toFixed(2)}`;

    // calls function to update the formsets
    updateInstrumentFormsets()
};


/**
 * @name addReviewSession
 * @description 
*/
function addReviewSession(ev){
    if (ev){
        ev.preventDefault();
    }
    // increasing the number of reviews (displayed and the input)
    numOfReviewsContainer.innerText = parseInt(numOfReviewsContainer.innerText)+1;
    numOfReviewsInput.setAttribute('value', parseInt(numOfReviewsInput.value)+1);

    // increases the displayed price
    displayPriceContainer.innerText = `£ ${(parseFloat(displayPriceContainer.innerText.replace('£', '')) + parseFloat(additionalReviewSessionPrice)).toFixed(2)}`;

    // checking which project was chosen and gettings its num_review_sessions
    let selectedProjectTypeText = projectTypeDropdown[projectTypeDropdown.options.selectedIndex].innerText;
    let projectMinNumOfReviews = document.getElementById(`num-included-reviews-${selectedProjectTypeText}`).innerText;

    // calling the checkReviewSessionButtons function
    checkReviewSessionButtons(numOfReviewsContainer.innerText, projectMinNumOfReviews, maxNumReviewSessions)
};


/**
 * @name subtractReviewSession
 * @description 
*/
function subtractReviewSession(ev){
    if (ev){
        ev.preventDefault();
    }
    // increasing the number of reviews (displayed and the input)
    numOfReviewsContainer.innerText = parseInt(numOfReviewsContainer.innerText)-1;
    numOfReviewsInput.setAttribute('value', parseInt(numOfReviewsInput.value)-1);

    // decreases the displayed price
    displayPriceContainer.innerText = `£ ${(parseFloat(displayPriceContainer.innerText.replace('£', '')) - parseFloat(additionalReviewSessionPrice)).toFixed(2)}`;

    // checking which project was chosen and gettings its num_review_sessions
    let selectedProjectTypeText = projectTypeDropdown[projectTypeDropdown.options.selectedIndex].innerText;
    let projectMinNumOfReviews = document.getElementById(`num-included-reviews-${selectedProjectTypeText}`).innerText;

    // calling the checkReviewSessionButtons function
    checkReviewSessionButtons(numOfReviewsContainer.innerText, projectMinNumOfReviews, maxNumReviewSessions)
};


/**
 * @name checkReviewSessionButtons
 * @description 
*/
function checkReviewSessionButtons(currentNumReviewSessions, projectMinNumOfReviews, maxNumReviewSessions){

    // if the current number of review sessions is equal to the minimum then the - button is disabled, else its enabled
    if (numOfReviewsContainer.innerText == projectMinNumOfReviews){
        subtractReviewSessionButton.disabled = true;
        subtractReviewSessionButton.classList.remove('btn-midi-warning');
        subtractReviewSessionButton.classList.add('btn-l-grey');
    } else {
        subtractReviewSessionButton.disabled = false;
        subtractReviewSessionButton.classList.add('btn-midi-warning');
        subtractReviewSessionButton.classList.remove('btn-l-grey');
    }

    // if the current number of review sessions is equal to the maximum then the + button is disabled, else its enabled
    if (numOfReviewsContainer.innerText == maxNumReviewSessions){
        addReviewSessionButton.disabled = true;
        addReviewSessionButton.classList.remove('btn-teal');
        addReviewSessionButton.classList.add('btn-l-grey');
    } else {
        addReviewSessionButton.disabled = false;
        addReviewSessionButton.classList.add('btn-teal');
        addReviewSessionButton.classList.remove('btn-l-grey');
    }
};


/**
 * @name toggleTestimonialTextContainer
 * @description 
*/
function toggleTestimonialTextContainer(ev){
    if (ev){
        ev.preventDefault();
    }

    // getting the testimonial-text-container
    let testimonialTextContainer = document.getElementById('testimonial-text-container');

    // checks if the checkbox is checked
    if(useAsTestimonialCheckbox.checked){
        testimonialTextContainer.classList.remove('d-none');
    } else {
        testimonialTextContainer.classList.add('d-none');
    }

};


/**
 * @name validateBpmInput
 * @description 
*/
function validateBpmInput(ev){
    if (ev){
        ev.preventDefault();
    }
    
    console.log('bpm input', ev.target.innerHTML)
    
};


/**
 * @name styleCurrentImageSection
 * @description 
*/
function styleCurrentImageSection(){
    
    let imageClearCheckbox = document.getElementById('image-clear_id');

    // adding start padding to the checkbox
    imageClearCheckbox.classList.add('ms-2');

    console.log('imageClearCheckbox NEXT SIBLING', imageClearCheckbox.nextElementSibling.innerText)
    // changing the label innerText
    imageClearCheckbox.nextElementSibling.innerText = 'Remove image';
    imageClearCheckbox.nextElementSibling.classList.add('text-capitalize', 'fs-6', 'fw-normal');

    console.log('imageClearCheckbox PREV SIBLING', imageClearCheckbox.previousElementSibling)

    // adding midi-teal class to the anchor element
    imageClearCheckbox.previousElementSibling.classList.add('midi-teal');

    // adding bottom margin to the label element
    imageClearCheckbox.nextElementSibling.classList.add('mb-2');
};
        