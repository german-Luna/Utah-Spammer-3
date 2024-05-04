import requests
import random
import string

def create_random_string(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

def submit_fake_complaint():
    url = 'https://webto.salesforce.com/servlet/servlet.WebToCase?encoding=UTF-8'

    payload = {
        'captcha_settings': '{"keyname":"HotlineWebtoCaseSFProd","fallback":"true","orgId":"00D41000002kUxv","ts":"1714850545738"}',
        'orgid': '00D41000002kUxv',
        'retURL': 'https://ut-sao-special-prod.web.app/success.html',
        'type': 'SP - Distinctions on the Basis of Sex',
        '00N1K00000fGn13': 'Ascent Academies of Utah',
        'cb1': '1',
        'cb2': '1',
        'cb3': '1',
        'cb4': '1',
        'cb5': '1',
        'cb6': '1',
        'cb7': '1',
        'cb8': '1',
        'cb9': '1',
        '00N1K00000fXXY2UAO': '',
        '00N1K00000fXXY1': '\n\n<strong>Violations applicable to all state and local governments</strong>\n<p>Government entity allowed an individual to access, use, or benefit from a government entity’s athletic facility, program, or event when the individual’s sex does not match the sex designation for the facility, program, or event<p> <br>\n<p>Government entity failed to contact law enforcement when criminal complaints (such as lewdness, voyeurism, loitering in a privacy space, etc.) were reported.<p> <br>\n<p>Government entity failed to adopt a privacy compliance plan to address compliance with the government entity’s duties under 63G-31.<p> <br>\n<p>Government entity failed to include a single occupant facility in new construction. Note: For existing privacy spaces, the government entity is required only to consider the feasibility of retrofitting or remodeling privacy spaces; it is not required to remodel/retrofit.<p> <br>\n<p>Other violation of Utah Code §63G-31. List the section of Utah Code §63G-31 you believe was violated in the details section below.</p> <br>\n<strong>Violations specifically applicable to public education (including charter schools)</<strong>>\n<p>Public school failed to provide equal quality, opportunity, or availability and scheduling of facilities, programs, and events for both sexes.</p> <br>\n<p>Public school required males or females to participate or compete against the opposite sex in any sex-designated facility, program, or event.</p> <br>\n<p>Public school required, gave official authorization for, or knowingly allowed males or females to use a sex-designated facility in the presence of the opposite sex.</p> <br>\nA local education agency failed to:\n\n++++++++++++<li>\n++++++++++++++++give notice to students of the provisions of Utah Code\n++++++++++++++++63G-31-30;\n++++++++++++</li>\n++++++++++++<li>\n++++++++++++++++take administrative action to address violations of and\n++++++++++++++++promote compliance with Utah Code 63G-31; or\n++++++++++++</li>\n++++++++++++<li>\n++++++++++++++++coordinate with a student’s parents or legal guardian to\n++++++++++++++++develop a privacy plan under Utah Code 63G-31-301(2).\n++++++++++++++++</li>\n++++++++++++++++<br>\n++++++++++++\n\n1. <strong>Who are the employees or officials at the government entity who were involved in the alleged noncompliance or who have the responsibility to remediate the alleged noncompliance or violation?</strong>\n<br>\n<p>{scnd_random_string}</p>\n<br>\n<br>\n\n<strong>2. Please provide the following information about the alleged violation(s): 1) Where did the violation occur? Identify the specific government operated or controlled location, facility, program, or event; 2) When did the noncompliance or alleged violation(s) occur? Is it on-going? and 3) Describe any other relevant circumstances and details of the alleged violation(s)</strong>\n<br>\n<p>{random_string}?</p>\n<br>\n<br>\n\n<strong>3. We encourage citizens to make reasonable attempts to address and resolve concerns directly with the government entity when possible. Please describe any measures you have taken to resolve these concerns, who you have communicated with, and any response provided by the entity.</strong>\n<br>\n<p>{random_string}</p>\n<br>\n<br>\n\n<strong>4. How do you know about the alleged noncompliance or violation(s)?</strong>\n<br>\n<p>seriously</p>\n<br>\n<br>\n\n<strong>5. What evidence exists to support your allegation? Please provide details</strong>\n<br>\n<p>its good</p>\n<br>\n<br>\n',
        'third-party-disclose-radio': 'on',
        '00N1K00000fHhTd': '1',
        '00N1K00000fX1ND': create_random_string(128),
        '00N1K00000fXXY3': create_random_string(128),
        '00N1K00000fWywZ': create_random_string(128),
        '00N1K00000fWywe': create_random_string(128),
        'external': '1',
        'g-recaptcha-response': create_random_string(128),
        'Submit Complaint': 'Submit',
        'recordType': '0121K000001Ae5QQAS',
        'Status': 'New Complaint'
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Spam Complaint submitted successfully!")
    else:
        print("Failed to submit spam complaint. Status code:", response.status_code)

if __name__ == "__main__":
    while True:
        submit_fake_complaint()
