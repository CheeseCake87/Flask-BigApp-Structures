document.addEventListener("alpine:init", () => {
    Alpine.store('darkMode', {
        on: Alpine.$persist('darkMode', false),
        toggle() {
            this.on = !this.on
        }
    })
});