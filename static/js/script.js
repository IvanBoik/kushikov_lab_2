
const input = document.getElementById("status-input")
input.value = sessionStorage.getItem("status") || ""

function random() {
    return Math.round(((Math.random() * 0.7 + 0.01) + Number.EPSILON) * 100) / 100
}

if (input.value !== "Выполнено") {
    for (let i=1; i<5; i++) {
        for (let j=1; j<5; j++) {
            let value = random()
            sessionStorage.setItem("faks-" + i + "-" + j, value)
            let el = document.getElementById("faks-" + i + "-" + j).value = value
        }
    }

    for (let i=1; i<16; i++) {
        let value = random()
        sessionStorage.setItem("init-eq-" + i, value)
        let init_eq_el = document.getElementById("init-eq-" + i).value = value
    }

    for (let i=1; i<56; i++) {
        for (let j=1; j<5; j++) {
            let value = random()
            sessionStorage.setItem("equations-" + i + "-" + j, value)
            let el = document.getElementById("equations-" + i + "-" + j).value = value
        }
    }
}
else {
    for (let i=1; i<5; i++) {
        for (let j=1; j<5; j++) {
            let el = document.getElementById("faks-" + i + "-" + j).value = sessionStorage.getItem("faks-" + i + "-" + j)
        }
    }

    for (let i=1; i<16; i++) {
        let init_eq_el = document.getElementById("init-eq-" + i).value = sessionStorage.getItem("init-eq-" + i)
    }

    for (let i=1; i<56; i++) {
        for (let j=1; j<5; j++) {
            let el = document.getElementById("equations-" + i + "-" + j).value = sessionStorage.getItem("equations-" + i + "-" + j)
        }
    }
}


function getFaks() {
    const faks = []

    for (let i=1; i<5; i++) {
        const temp = []
        for (let j=1; j<5; j++) {
            let el = document.getElementById("faks-" + i + "-" + j).value
            temp.push(el)
        }
        faks.push(temp)
    }
    return faks
}

function getInitialEquations() {
    const init_eq = []

    for (let i=1; i<16; i++) {
        let init_eq_el = document.getElementById("init-eq-" + i).value
        init_eq.push(init_eq_el)
    }
    return init_eq
}

function getRestrictions() {
    const restrictions = []

    for (let i=1; i<16; i++) {
        let restrictions_el = document.getElementById("restrictions-" + i).value
        restrictions.push(restrictions_el)
    }
    return restrictions
}

function getEquations() {
    const equations = []

    for (let i=1; i<56; i++) {
        const temp = []
        for (let j=1; j<5; j++) {
            let el = document.getElementById("equations-" + i + "-" + j).value
            temp.push(el)
        }
        equations.push(temp)
    }
    return equations
}


async function process() {
    const faks = getFaks()
    const init_eq = getInitialEquations()
    const restrictions = getRestrictions()
    const equations = getEquations()

    console.log(JSON.stringify({
                "faks": faks,
                "initial_equations": init_eq,
                "restrictions": restrictions,
                "equations": equations
            }))
    const response = await fetch('/draw_graphics', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "faks": faks,
                "initial_equations": init_eq,
                "restrictions": restrictions,
                "equations": equations
            })
        })

        const result = await response.json()
        input.value = result.status
        sessionStorage.setItem("status", result.status)
}