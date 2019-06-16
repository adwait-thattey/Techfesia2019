
function lowerAndRemoveReqChars(inpStr){
    const replaceSubs = {
        " ": "-"
    };

    const delSubs = ['(', ')'];

    inpStr = inpStr.toLowerCase();
    for(key in replaceSubs){
        inpStr = inpStr.split(key).join(replaceSubs[key]);
    }
    for(ch of delSubs){
        inpStr = inpStr.split(ch).join('');
    }

    return inpStr;
}


$(document).ready(function () {
    const folders = postmanData.item;
    for (const folder of folders) {
        const folderNameFormatted = lowerAndRemoveReqChars(folder.name);
        console.log(folderNameFormatted);

        const requests = folder.item;
        for (req of requests) {
            if (req.request.description) {
                // console.log(req.name);
                // console.log(req.request.description);

                const reqNameFormatted = lowerAndRemoveReqChars(req.name);
                const reqId = ['request', folderNameFormatted, reqNameFormatted].join('-');
                console.log(reqId);
                let descriptionFormatted = req.request.description.split('\n').join('<br>');

                // remove extra line break in a list
                descriptionFormatted = descriptionFormatted.split('</li><br>').join('</li>');
                const descriptionElement = `
                                                <div style="font-style:italic">
                                                    <blockquote>
                                                        ${descriptionFormatted}
                                                    </blockquote>
                                                </div>
                                                `
                const element = document.getElementById(reqId).insertAdjacentHTML("afterend", descriptionElement);
            }
        }
    }
});

$(document).ready(function () {
    allPanes = document.getElementsByClassName("tab-pane")
    for (pane of allPanes) {
        if (pane.id.includes("http")) {
            pane.classList.add("active");
        }
        else if (pane.id.includes("curl")) {
            pane.classList.remove("active");
        }

        allTagPanes = document.getElementsByTagName("li");

        curlTagPanes = [];
        for (l of allTagPanes) {
            if (l.innerText == "Curl") {
                curlTagPanes.push(l);
            }
        }

        httpTagPanes = [];
        for (l of allTagPanes) {
            if (l.innerText == "HTTP") {
                httpTagPanes.push(l);
            }
        }

        for (l of curlTagPanes) {
            l.classList.remove("active");
        }

        for (l of httpTagPanes) {
            l.classList.add("active");
        }
    }

    // curlPane = document.getElementById("request-authentication-superuser-token-refresh-example-curl");

    // curlPane.classList.remove("active");
});
