// Get rid of "activities completed" at the bottom since students assume that's what we
// use to track completion credit for runestone, but it's not. Activities completed includes
// things like clicking on all the hint buttons, file preview buttons, starting all the YouTube
// videos, etc. which we don't want to require, so we have separate assignments instead.
$(() => $("#scprogresscontainer").hide());
$(() => $("#completionButton").hide());