Python scripts I have written to automate tests performed for City of Heroes using the chat log file. 

## Crit Test and Proc Rate Test ##

These two scripts employ the exact same instances function, and work in essentially the same way. Use them to test how often you crit or how often a proc fires versus how many attacks were performed. 

## Endurance Procs Test ##

This script was written specifically to test how often various endurance procs fire, such as Panacea and Performance Shifter. Idle in your base for hours and run this on your log. Easily modified for health instead of endurance. 

## PPM Test ##

Very similar to the proc rate test script but written to compute average PPM (procs per minute), rather than procs per attacks used. 

## DPS Test ##

A bit complicated, but this script can be used to compute the exact dps done in a variety of combinations. For instance: 

- The dps done by you overall
- The dps done by you to a specific target
- Either of the above two using a specific power
- The dps done to you overall
- The dps done by a specific target to you
- Either of the above two with a specific power

In addition, it can be used to output total damage instead of dps, as well as output an entire log of the relevant combat log lines. 

## Hit Roll Test ##

This script was written to test the game's RNG. Specify an attack you wish to test, find a target to leave it on auto with for a few hours (Rikti Warzone practice dummies are ideal), and then run this on your log. It will generate two png images (saved to the same directory as the script) graphing the cumulative hit rate as a function of total number of hits, one factoring in streakbreaker, one not. It will also print the average hit rate from the start of the test to the present when ran. 
