function clearActiveAnnotationLinks(element) {
    if (element.getAttribute('data-annotation-stack-is-shown') !== null) {
        element.setAttribute('data-annotation-stack-is-shown', "false");
    }
    for (let childElem of element.children) {
        clearActiveAnnotationLinks(childElem);
    }
}

function showBuddy(element) {
    let wasActive = element.getAttribute('data-annotation-stack-is-shown');
    let docElem = document.getElementById(element.getAttribute("data-doc-id"));
    clearActiveAnnotationLinks(docElem);
    let anno = document.getElementById(
        element.getAttribute('data-annotation-stack-id')
    );
    let annoSibling = anno.parentNode.firstElementChild;
    while (annoSibling !== null) {
        annoSibling.setAttribute("data-is-selected", "false");
        annoSibling = annoSibling.nextElementSibling;
    }
    if (wasActive !== "true") {
        element.setAttribute('data-annotation-stack-is-shown', "true");
        anno.setAttribute("data-is-selected", "true");
    }
}
