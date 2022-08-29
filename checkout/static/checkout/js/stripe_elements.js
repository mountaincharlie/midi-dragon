// jshint esversion: 6

/**
 * CREDITS
 * 
 * [Setup Stripe.js and Submit the payment to Stripe section] https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements
 * 
 * Logic adapted from CI walkthrough
 * https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/933797d5e14d6c3f072df31adf0ca6f938d02218/checkout/static/checkout/js/stripe_elements.js
 */


// ---- GLOBAL VARS

// getting stripe_public_key and client_secret text without first and last chars (the '')
let stripePublicKey = document.getElementById('id_stripe_public_key').innerText.slice(1, -1);
let clientSecret = document.getElementById('id_client_secret').innerText.slice(1, -1);

// console.log('stripePublicKey', stripePublicKey)
// console.log('clientSecret', clientSecret)

// let clientSecret = $('#id_client_secret').text().slice(1, -1);
// let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);

// using stripe's builtin JS to setup Stripe with our stripePublicKey
let stripe = Stripe(stripePublicKey);
// create instance of stripe elements
let elements = stripe.elements();


// the card element can accept a style argument
var style = {
    base: {
        color: '#9A9EAE',
        backgroundColor: '#1D212E',
        iconColor: '#00D1CF',
        // fontFamily: '"BioRhyme", sans-serif',
        fontSize: '16px',
        '::placeholder': {
            color: '#9A9EAE',
            // fontFamily: '"BioRhyme", sans-serif',
        }
    },
    invalid: {
        // using midi-warning class color
        color: '#fc5a5a',
        iconColor: '#fc5a5a'
    }
};

// creates, styles and mounts the Stripe card element
var card = elements.create('card', {style: style});
// using stripe's method to mount the card to the #card-element div 
card.mount('#card-element');


// ------ handling real-time errors on card element

/**
 * Applying a 'change' event listener to the card element
 * Checks for errors everytime the card elements input changes
 * -gets the card-errors div (near card div on checkout page)
 * so that if there are errors they can be displayed to the user
 * through this
 * -if theres an error in the event, the message is created and put into
 * the card-errors div
*/

card.addEventListener('change', function(ev) {
    let errorDiv = document.getElementById('card-errors');
    console.log('errorDiv', errorDiv)
    if (ev.error) {
        let error_msg_html = `
            <span role="alert">
                <i class="fa-solid fa-circle-xmark"></i>
            </span>
            <span>${ev.error.message}</span>
        `
        errorDiv.innerHTML = error_msg_html;
    } else {
        errorDiv.innerText = '';
    }
});


