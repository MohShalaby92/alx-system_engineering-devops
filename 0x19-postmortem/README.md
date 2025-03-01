# How A Single Letter Took Down Our Entire Website :man_facepalming:

## Our company's most expensive typo of the year*

## Issue Summary
**Duration**: February 28, 2025, 21:29:59 GMT - February 28, 2025, 22:45:00 GMT (1 hour 15 minutes)  
**Impact**: The company website performed its best disappearing act yet, serving nothing but HTTP 500 errors to all visitors. 100% of users were affected, with approximately 1,200 people wondering if we'd gone out of business.  
**Root Cause**: A rogue 'p' sneaked into our codebase! A typographical error in the WordPress configuration file (wp-settings.php) tried to include "class-wp-locale.phpp" instead of the correct "class-wp-locale.php". As it turns out, computers are extremely literal and don't autocorrect our typos like smartphones do.

## Timeline: The Hunt for the Phantom 'P'
* **21:29:59 GMT** - Monitoring system starts frantically alerting about 500 errors (essentially saying "MAYDAY! MAYDAY!")
* **21:35:00 GMT** - On-call engineer reluctantly puts down dinner fork and begins investigating
* **21:40:00 GMT** - Apache error logs inspected and unhelpfully show nothing of interest (very helpful, Apache!)
* **21:45:00 GMT** - Web server status check confirms Apache is running fine and pointing fingers elsewhere
* **21:50:00 GMT** - Database connection verified as working properly (first red herring caught and released)
* **22:00:00 GMT** - System resources checked - plenty of CPU, memory, and disk space (second red herring)
* **22:10:00 GMT** - HTTP headers inspected, revealing PHP is processing requests but responding with 500 errors
* **22:15:00 GMT** - Incident escalated to Web Platform team with the message "HELP! PHP is broken but not broken?"
* **22:25:00 GMT** - Test PHP file created and works perfectly (the plot thickens)
* **22:30:00 GMT** - Strace deployed - when regular debugging fails, trace EVERYTHING
* **22:35:00 GMT** - PHP configuration modified to display errors instead of failing silently (why wasn't this the default?)
* **22:40:00 GMT** - Culprit identified: a tiny, innocent-looking 'p' at the end of ".php" extension
* **22:45:00 GMT** - Issue resolved by banishing the extra 'p' from the filename using the mighty sed command


The Debugging Journey:

Start → Check Logs → :thinking: → Check Server → :thinking: → Check Database → :thinking:
→ Check Resources → :thinking: → Check Headers → :thinking: → Test PHP → :thinking: 
→ Use Strace → :thinking: → Enable Error Display → :bulb: → Find Typo → :tada:

## Root Cause and Resolution
The WordPress settings file tried to load a non-existent file because someone accidentally typed `class-wp-locale.phpp` with an extra 'p'. This is the digital equivalent of asking someone to grab your coffee from the kitchenette when it's actually in the kitchenp - they'll come back empty-handed and confused.

Our silent PHP configuration was the accomplice, hiding the error details and returning a mysterious 500 status instead of simply saying "Hey, I can't find this file you asked for!"

The fix was elegantly simple: `sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php`. One command, one second to run, and 75 minutes of debugging time. Because that's how IT works!

## Corrective and Preventative Measures
**Improvements Needed**:
* Make PHP error logging more verbose than a teenager explaining why they missed curfew
* Implement monitoring that tells us WHY things are broken, not just THAT they're broken
* Establish actual deployment processes instead of "yolo git push to production"
* Create automated testing for configuration files (computers are good at finding typos, let's use them)
* Improve our incident response procedures for faster resolution
* Enhance debugging capabilities in production environments

**Specific Action Items**:
1. Configure PHP to log errors to a dedicated file instead of silently weeping into stderr
2. Add log monitoring alerts that actually point to the problem
3. Create a Puppet manifest to ensure WordPress file integrity checks
4. Implement pre-deployment syntax checking for all PHP files
5. Enable detailed error reporting in staging that would have caught this in 5 seconds
6. Create a documentation page titled "So Your WordPress Site Is Returning 500 Errors"
7. Add automated tests that verify included files exist before deploying
8. Schedule monthly error log reviews (with pizza provided to ensure attendance)
9. Develop a troubleshooting checklist for web application failures
10. Train team on debugging tools like strace (with actual hands-on exercises)
11. Implement standard process for enabling verbose errors during incidents

Remember: In the epic battle between humans and computers, a single typo can bring a website to its knees.
