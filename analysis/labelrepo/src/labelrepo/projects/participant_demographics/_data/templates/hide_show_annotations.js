function hideAnnotations(element) {
    element.querySelectorAll(
        "*[data-annotation-stack-is-shown='true']").forEach(
        (elem) => {
            elem.setAttribute("data-annotation-stack-is-shown", "false");
            const allAnnoIds = elem.getAttribute(
                'data-annotation-stack-ids').split(",");
            allAnnoIds.forEach((annoId) => {
                document.getElementById(annoId).setAttribute(
                    "data-is-selected", "false");
            });
        }
    );
}

function showBuddy(element) {
    const wasActive = element.getAttribute('data-annotation-stack-is-shown');
    const docElem = document.getElementById(element.getAttribute("data-doc-id"));
    hideAnnotations(docElem);
    if (wasActive !== "true") {
        element.setAttribute('data-annotation-stack-is-shown', "true");
        const allAnnoIds = element.getAttribute(
            'data-annotation-stack-ids').split(",");
        allAnnoIds.forEach((annoId) => {
            document.getElementById(annoId).setAttribute(
                "data-is-selected", "true");
        });
    }
}

function addDetailsEvents() {
    const allDetails = document.querySelectorAll(
        ".labelrepo-debug-details details");
    allDetails.forEach((details) => {
        details.addEventListener("toggle", (event) => {
            if (event.target.hasAttribute("open")){
                return;
            }
            hideAnnotations(event.target);
        });
    });
}

window.addEventListener("DOMContentLoaded", addDetailsEvents);
