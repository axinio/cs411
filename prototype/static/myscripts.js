let problems = new Array ()
function obliterate(obj){
    var total_meds = []
    let keys = Object.keys(obj); 
    total_meds = keys
    for(var prop in obj){
        if(typeof obj[prop]=='object'){
            for(var x in obj[prop]){
                if(obj[prop][x] != null){
                    problems.push([prop,x,obj[prop][x]])
                    }
                }
                if (total_meds.includes(x)==false){
                    total_meds.push(x);
                }
            }
        
    }

    console.log(keys)
    console.log(problems)
    console.log(total_meds)
    return [total_meds]
    
}

async function loadNames(a) {
  const response = await fetch(a);
  const names = await response.json();
  return names
}

function interactionDisplay(asso,total){
    for (i in total){
    for (x in asso){
        if (asso[x].includes(total[i])){
            document.getElementById(asso[x][0]).style.color = 'red'
            document.getElementById(asso[x][1]).style.color = 'red'
            console.log("activated")
        }
    }
};
}


 async function addMark(data){
    a = obliterate(data)
    total_meds =  a[0]
    for (var x in total_meds){
        a = 'https://rxnav.nlm.nih.gov/REST/rxcui/' + total_meds[x] + '.json'
        var testing = await loadNames(a)
        var new_name = testing.idGroup.name
        var myEle = document.getElementById(total_meds[x]);
        if (myEle == null) {
        $('#test').append(
            $(document.createElement('input')).prop({
                name: new_name,
                type: 'checkbox'
                
            })
        ).append(
            $(document.createElement('label')).prop({
                id: total_meds[x],
                for: total_meds[x]
            }).html(new_name)
            ).append(document.createElement('br'));
        } else {

        }

    }
    interactionDisplay(problems,total_meds)
    
};
    


