

# AI Challenge: Monster Engagements

The spirits roam and zombies rise; the undead seek revenge. Extant remains of fallen coders hunt for all who live. In buildings once the pride of Man the spiders now spin webs. In fields once green the ghouls convene, destroying all who pass.

The hope remains in one last stand, a battle for it all. The future lies in what's to come, and future’s coming fast. If humans win, the monsters pledge to rest forty-two years. If monsters win the humans DIE and then will cease to be.

You are part of the last resistance. On you depends the fate of humanity; Posterity begs your success! Being an AI-master, you set out to develop a tool which will be furnished by every man, woman, and child in your army--a portable battle assessor. The gadget will work like so:

Given the number of each respective monster attacking the person carrying the gadget (zombies, spirits, spiders, and ghouls) and his or her Strength (0-9 scale), it will predict whether the person or the monsters will win the engagement. An example:

Given this data,

Strength - 7; Zombies - 3;
Spirits - 2;
Spiders - 3;
Ghouls - 1,

your gadget should predict either ‘1’ for human win or ‘0’ for monster win.

With this tool, your fighters will know when to start a fight or when to run and seek backup. The effectiveness of this tool will decide the fate of the battle.

HUMANITY DEPENDS ON YOU.

Problem restated:

You must develop a Python function predict(strength, num_zombies, num_spirits, num_spiders, num_ghouls) which outputs either the number ‘1’, meaning the human should win the fight, or ‘0’ meaning the monsters should win the fight. Ensure the function argument names match the ones I have listed here: strength, num_zombies, num_spirits, num_spiders, num_ghouls.

You will be given

* A dataset containing examples wherein the human won an engagement and examples wherein the monsters won an engagement. Each entree is formatted [[#zombies,#spirits,#spiders,#ghouls],outcome]
* An example function which (poorly) addresses the problem at hand.
* A script to evaluate your functions performance. (This is NOT the same evaluator your function will ultimately face)

Constraints:

* Your function must be a callable Python function. You are allowed to use all built-in Python libraries and no external libraries. (However, this does NOT mean that you cannot use other libraries to help develop your function; you CAN and SHOULD try using Tensorflow to develop a model for making predictions)
* Your function must be called “predict”.
* Your function must always output either ‘1’ or ‘0’ as an integer value.

Evaluation:

* A function’s score is its proportion of correct predictions on a dataset I have stashed away for the evaluation phase of this challenge. The evaluation dataset is of the same distribution of the dataset I provided you.
