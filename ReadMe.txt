# README - Using Social BINGO

## Why create Social BINGO Cards this way?

Social BINGO is an ice breaker game in which players try to meet people who meet specific objectives. A tile on a BINGO card might say something like "Enjoys Pastrami". When the player meets someone who enjoys pastrami, they mark that tile as completed and perhaps record the name of the player.

Whenever I see a game of Social BINGO, I see the same 24 questions listed on all players cards. The cards are shuffled, sure - but everyone has the same questions listed. This leads to repeating patterns: once one person is identified as loving pastrami, several people might use that same person to complete the square. I think this is a problem that creates an off-balance experience for players.

Think about a classic numbered BINGO game:

* Each card has 5 numbers in a column (or 4 for N to allow the Free Tile).
* There are 20 possible results in each column.

That means that only 1 in 4 drawn Bingo Balls will appear on any given Bingo Card.

* Results do not cross columns. (For example, the number "12" is always under the "B" column.)

That means that each column is a category of information that people can more easily identify.

My challenge in creating this package is to make a robust Social BINGO game that accurately reflects the excitement and randomized nature of traditional BINGO to maximize networking potential while minimizing work to create it.

Yes, this means thinking of more creative questions -- but using this tool, it won't take too much more work. And I think the payoff will be worth it.


## Customize your BINGO tiles.

Edit the bingo tile options to your liking. They can be found in the Input folder. There are several different files, each representing a column on BINGO cards.

Each entry must be listed on a different line - but the number of lines is up to you. Just make sure you have a minimum of five per document (or at least four for N and one for Free Space). I suggest creating many more than necessary. Remember: Classic BINGO has 20 per column!

This version of Social BINGO uses the same unique-set-per-column concept. To reflect the idea that results do not cross columns, I suggest having a theme for each list. I think this helps to ensure all participants are getting a well rounded experience.

The default values in this repository reflect the following:
* B is for Background
* I is for Interests
* N is for Notable Achievements
* G is for Guilty Pleasures
* O is for Oddities and Quirky Behaviour

But feel free to play around with them!


## Run the Update Script

Run "Update Script" to regenerate and randomize the BINGO cards. This will update the csv document in the Output folder. If you're using this BINGO generator in another context where results are drawn for everyone at once, you can use this file to track the legitimacy of winners. (#todo Create a way to track vertical/horizontal lines, corners, X shapes, and box shapes.)

By default, this script creates 80 randomized cards and then removes duplicates so that no two cards are alike.

## Print The BINGO Cards

The MS Word file uses MailMerge to create printable Bingo cards from the data in the Output folder. I suggest saving them to PDF first, and then printing multiple pages on single sheets using the print settings in Chrome or Acrobat.
