from pathlib import Path
p=Path('/mnt/data/working/v9edit/index.html')
s=p.read_text()
s=s.replace('<title>Home | Digging Britannia</title><link rel="stylesheet" href="styles.css">', '<title>Home | Digging Britannia</title><link rel="stylesheet" href="styles.css"><link rel="stylesheet" href="https://sibforms.com/forms/end-form/build/sib-styles.css">')
old='''<section class="signup-section"><div class="container"><div class="signup-card reveal"><div class="signup-copy"><div class="section-kicker">Stay in the loop</div><h2>Never Miss a Dig</h2><p>Want to know when a new Digging Britannia dig is announced? Join our free updates list and we'll let you know about new digs and important group announcements.</p><p class="signup-note">You can unsubscribe from our email updates at any time using the link in our emails.</p></div><div class="brevo-form-wrap"><iframe width="540" height="305" src="https://45d98b5d.sibforms.com/v2/serve/MUIFAITEC45MTAPKP_q4eqwpeP46JH9W71G9s37ANUcyvuHr0S4TMbI2JzPV5OL1ZrsuCmsWvFBak0OBzJWXSwqZtdeeo5V3iLmfeHs_0lR9tgLwK22ISnD3ZeSUrRTeb8tEFfeRAxn__6hFN60mdWgFcjBkkFlhzj0LlQvGN_9qfRcMJjfA8hzAzaWPYZyOWZwxU4PTrxuNR2ooQA==" frameborder="0" scrolling="auto" allowfullscreen title="Digging Britannia email signup form"></iframe></div></div></div></section>'''
new='''<section class="signup-section"><div class="container"><div class="signup-card reveal">
<div class="signup-copy"><div class="section-kicker">Stay in the loop</div><h2>Never Miss a Dig</h2><p>Want to know when a new Digging Britannia dig is announced? Join our free updates list and we'll let you know about new digs and important group announcements.</p><p class="signup-note">You can unsubscribe from our email updates at any time using the link in our emails.</p></div>
<div class="brevo-html-form">
  <div id="sib-form-container" class="sib-form-container">
    <div id="error-message" class="sib-form-message-panel" role="alert"><div class="sib-form-message-panel__text sib-form-message-panel__text--center">Your information could not be saved. Please try again.</div></div>
    <div id="success-message" class="sib-form-message-panel" role="status"><div class="sib-form-message-panel__text sib-form-message-panel__text--center">Thanks for signing up!</div></div>
    <div id="sib-container" class="sib-container--large sib-container--vertical">
      <form id="sib-form" method="POST" action="https://45d98b5d.sibforms.com/serve/MUIFAITEC45MTAPKP_q4eqwpeP46JH9W71G9s37ANUcyvuHr0S4TMbI2JzPV5OL1ZrsuCmsWvFBak0OBzJWXSwqZtdeeo5V3iLmfeHs_0lR9tgLwK22ISnD3ZeSUrRTeb8tEFfeRAxn__6hFN60mdWgFcjBkkFlhzj0LlQvGN_9qfRcMJjfA8hzAzaWPYZyOWZwxU4PTrxuNR2ooQA==" data-type="subscription">
        <div class="sib-form-block signup-form-intro"><p>Join the Digging Britannia updates list.</p></div>
        <div class="sib-input sib-form-block">
          <div class="form__entry entry_block">
            <div class="form__label-row"><label class="entry__label" for="EMAIL" data-required="*">Email address</label><div class="entry__field"><input class="input" type="email" id="EMAIL" name="EMAIL" autocomplete="email" value="" placeholder="you@example.com" data-required="true" required></div></div>
            <label class="entry__error entry__error--primary"></label>
            <label class="entry__specification">We'll only use your email for Digging Britannia updates.</label>
          </div>
        </div>
        <div class="sib-optin sib-form-block" data-required="true">
          <div class="form__entry entry_mcq">
            <div class="entry__choice"><label><input type="checkbox" class="input_replaced" value="1" id="OPT_IN" name="OPT_IN" required><span class="checkbox checkbox_tick_positive"></span><span class="optin-copy"><p>I agree to receive Digging Britannia updates and announcements by email and accept the data privacy statement.</p></span></label></div>
            <label class="entry__error entry__error--primary"></label>
            <label class="entry__specification">You may unsubscribe at any time using the link in our newsletter.</label>
          </div>
        </div>
        <div class="sib-form__declaration"><div class="declaration-block-icon"><span class="declaration-shield">✓</span></div><div><p>We use Brevo as our marketing platform. By submitting this form you agree that the personal data you provided will be transferred to Brevo for processing in accordance with <a href="https://www.brevo.com/en/legal/privacypolicy/" target="_blank" rel="nofollow noopener">Brevo's Privacy Policy.</a></p></div></div>
        <div class="sib-form-block submit-wrap"><button class="sib-form-block__button sib-form-block__button-with-loader" form="sib-form" type="submit"><svg class="icon clickable__icon progress-indicator__icon sib-hide-loader-icon" viewBox="0 0 512 512" aria-hidden="true"><path d="M460.116 373.846l-20.823-12.022c-5.541-3.199-7.54-10.159-4.663-15.874 30.137-59.886 28.343-131.652-5.386-189.946-33.641-58.394-94.896-95.833-161.827-99.676C261.028 55.961 256 50.751 256 44.352V20.309c0-6.904 5.808-12.337 12.703-11.982 83.556 4.306 160.163 50.864 202.11 123.677 42.063 72.696 44.079 162.316 6.031 236.832-3.14 6.148-10.75 8.461-16.728 5.01z"/></svg>JOIN THE DIGS</button></div>
        <input type="text" name="email_address_check" value="" class="input--hidden"><input type="hidden" name="locale" value="en">
      </form>
    </div>
  </div>
</div></div></div></section>'''
if old not in s:
    raise SystemExit('old section not found')
s=s.replace(old,new)
script='''<script>\nwindow.REQUIRED_CODE_ERROR_MESSAGE='Please choose a country code';window.LOCALE='en';window.EMAIL_INVALID_MESSAGE=window.SMS_INVALID_MESSAGE='The information provided is invalid. Please review the field format and try again.';window.REQUIRED_ERROR_MESSAGE='This field cannot be left blank. ';window.GENERIC_INVALID_MESSAGE='The information provided is invalid. Please review the field format and try again.';window.INVALID_NUMBER='The information provided is invalid. Please review the field format and try again.';window.INVALID_DATE='Please enter a valid date';window.REQUIRED_MULTISELECT_MESSAGE='Please select at least 1 option';window.translation={common:{selectedList:'{quantity} list selected',selectedLists:'{quantity} lists selected',selectedOption:'{quantity} selected',selectedOptions:'{quantity} selected'}};var AUTOHIDE=Boolean(0);</script><script defer src="https://sibforms.com/forms/end-form/build/main.js"></script>'''
s=s.replace('</footer><script src="data.js"></script><script src="app.js"></script></body></html>', '</footer><script src="data.js"></script><script src="app.js"></script>'+script+'</body></html>')
p.write_text(s)
