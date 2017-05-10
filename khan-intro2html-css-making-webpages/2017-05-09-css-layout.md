# CSS layout

- grouping elements
- width height overflow
- box model
- position
- CSS in the wild: Googple Maps
- CSS floating elements

## CSS grouping elements

```
<span class="info"> in line </span>
```

```
<div id="block-info"> block </div>
```

[demo of "CSS grouping elements" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/demo-of-css-grouping-elements/4525115651194880)

[exercise of "Challenge: Group the groupers" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/exercise-of-challenge-group-the-groupers/5805571298361344)

## CSS width, height, and overflow

```
<style>
    .lovey-dovey {
        color: red;
    }

    #official-info {
        background: rgb(230, 230, 230);
        width: 70%;
        height: 180px;
        overflow-y: auto;
        overflow-x: hidden;
        <!-- overflow: visible; -->
    }

    #cute-cat {
        width: 120px;
    }
</style>
```

[Demo of "CSS width, height, and overflow" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/demo-of-css-width-height-and-overflow/6370073614024704)

[Exercise of "The overflowing ocean" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/exercise-of-the-overflowing-ocean/6039830357409792)

## CSS box model

![box-model](https://www.kasandbox.org/programming-images/misc/boxmodel.png)

```
<style>
    .lovey-dovey {
        color: red;
    }

    #official-info {
        background: rgb(230, 230, 230);
        width: 70%;
        height: 180px;
        overflow-y: auto;
        overflow-x: hidden;
        margin: 15px 0px 10px 6px;
        border: 2px dashed rgb(161, 161, 161);
        padding: 6px;
    }

    #cute-cat {
        width: 120px;
        margin-right: 10px;
        margin-bottom: 10px;
        border: 6px ridge red;
    }

    #container {
        width: 400px;
        margin: auto;
        border: 1px solid rgb(145, 0, 0);
        border-top: 10px solid purple;
        padding: 15px;
    }
</style>
```

[Demo of "CSS box model" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/demo-of-css-box-model/4703213986316288)

[Exercise of "Challenge: The boxer model" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/exercise-of-challenge-the-boxer-model/5287266724675584)

## CSS position

```
<style>
body {
    font-family: fantasy;
    color: rgb(199, 177, 14);
}

#landscape {
    width: 250px;
    position: absolute;
    top: 20px;
    left: 10px;
    z-index: 1; <!-- 底层位置-->
}

#winston {
    position: absolute;
    top: 50px;
    left: 50px;
    z-index: 2;
}
#hopper {
    position: absolute;
    top: 30px;
    left: 80px;
    z-index: 3;
}

h1 {
    position: fixed;
    z-index: 4;
    left: 30px;
}

#song {
    position: relative;
    top: 220px;
}
</style>
```

[Demo of "CSS position" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/demo-of-css-position/5219292340879360)

[Exercise of "Challenge: Position planet" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/exercise-of-challenge-position-planet/5855873066139648)

## CSS floating elements

[Demo of "CSS floating elements" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/demo-of-css-floating-elements/6566183649476608)

```
<style>
#hopper-pic {
    width: 100px;
    float: left;
    margin-right: 6px;
    margin-bottom: 6px;

}
#hopper-footer {
    background-color: rgb(232, 232, 232);
    padding: 6px;
    clear: both;
}

#hopper-links {
    float: right;
    width: 30%;
    margin-left: 10px;
}
</style>
</head>
```

[(10) Exercise of "Challenge: Floating clouds" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/exercise-of-challenge-floating-clouds/6101306959003648)

---

```
  @anifacc
  2017-05-10
```
