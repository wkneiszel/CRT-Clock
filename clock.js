
function randomInteger(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

var backGroundFiles = ["anne.jpg", "barbershop.jpg", "beach.jpg", "binoc.jpg", "binocside.jpg", "boston.jpg", "brigwiz.jpg", "brigwiz2.jpg", "camp.jpg", "canoe.jpg", "chomp.jpg", "city.jpg", "cowboy.jpg", "deer.jpg", "dino.jpg", "disco.jpg", "fish.jpg", "fish2.jpg", "fishing.jpg", "fog.jpg", "gate.jpg", "icechomp.jpg", "lazydog.jpg", "lunch.jpg", "nerds.jpg", "organ.jpg", "paddleboy.jpg", "pretzel.jpg", "road.jpg", "rocks.jpg", "scream.jpg", "signs.jpg", "stars.jpg", "street.jpg", "thumbsup.jpg", "tunnel.jpg", "tunnel2.jpg", "turtle.jpg", "typewriter.jpg"];
var hourFiles = ["dice.png", "text.png", "toon.png"];
var minuteOnesFiles = ["text.png", "toon.png"];
var minuteTensFiles = [
    ["hand.png", "oh.png", "text.png", "toon.png"],
    ["hand.png", "dice.png", "toon.png"],
    ["dice.png", "hand.png", "text.png", "text2.png", "toon.png"],
    ["dice.png", "hand.png", "text.png", "text2.png", "toon.png"],
    ["dice.png", "hand.png", "text.png", "toon.png"],
    ["dice.png", "hand.png", "text.png", "toon.png"]
];
var flavorFiles = ["already.png", "dontpanic.png", "hanginthere.png", "relax.png", "thetimeisnow.png", "timeforabreak.png"];
var colonFiles = ["text.png", "toon.png"];
var amPmFiles = ["text.png", "toon.png"];

function drawTime() {
    var c = document.getElementById("screen");
    var ctx = c.getContext("2d");

    // Set up coordinates
    var useFlavor = randomInteger(0, 5) == 0;
    minY = 10;
    if (useFlavor)
        minY = 74;
    var x = randomInteger(10, 128);
    var y = randomInteger(minY, 176);

    // Calculate time strings
    var now = new Date(Date.now());
    var hour = (now.getHours() % 12).toString().padStart(2, "0");
    var minuteTens = now.getMinutes().toString().padStart(2, "0").substring(0, 1);
    var minuteOnes = now.getMinutes().toString().padStart(2, "0").substring(1, 2);
    var amPm = (now.getHours() / 12) > 1 ? "pm" : "am";

    var bgImg = new Image;
    bgImgName = backGroundFiles[randomInteger(0, backGroundFiles.length - 1)]
    bgImg.src = "./images/" + bgImgName;
    bgImg.onload = function () {
        // Draw background image
        ctx.drawImage(bgImg, 0, 0);

        // Draw foreground sprites
        if (useFlavor) {
            var flavorImg = new Image;
            flavorImg.src = "./flavor/" + flavorFiles[randomInteger(0, flavorFiles.length - 1)];
            flavorImg.onload = function () {
                ctx.drawImage(flavorImg, 10, 10);
            }
        }

        var hourImg = new Image;
        hourImg.src = "./hours/" + hour + "/" + hourFiles[randomInteger(0, hourFiles.length - 1)];
        hourImg.onload = function () {
            ctx.drawImage(hourImg, x, y);
        }

        var colonImg = new Image;
        colonImg.src = "./colon/" + colonFiles[randomInteger(0, colonFiles.length - 1)];
        colonImg.onload = function () {
            ctx.drawImage(colonImg, x + 64, y);
        }

        var minuteTensImg = new Image;
        minuteTensImg.src = "./minute-tens/" + minuteTens + "/" + minuteTensFiles[minuteTens][randomInteger(0, minuteOnesFiles.length - 1)];
        minuteTensImg.onload = function () {
            ctx.drawImage(minuteTensImg, x + 96, y);
        }

        var minuteOnesImg = new Image;
        minuteOnesImg.src = "./minute-ones/" + minuteOnes + "/" + minuteOnesFiles[randomInteger(0, minuteOnesFiles.length - 1)];
        minuteOnesImg.onload = function () {
            ctx.drawImage(minuteOnesImg, x + 128, y);
        }

        var amPmImg = new Image;
        amPmImg.src = "./ampm/" + amPm + "/" + amPmFiles[randomInteger(0, amPmFiles.length - 1)];
        amPmImg.onload = function () {
            ctx.drawImage(amPmImg, x + 160, y);
        }
    }
}

window.onload = function () {
    drawTime();
    setInterval(() => drawTime(), 20000);
}
