document.addEventListener('alpine:init', () => {

    Alpine.store('fragmentor', {
        async get(url, inject_el) {
            const fetcher = await fetch(url).catch(error => {
                console.log(error);
            });
            if (fetcher.status === 200) {
                inject_el.innerHTML = await fetcher.text();
            }
        }
    });

});