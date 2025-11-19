/**
 * Handle the "Create Task" form submission.
 * Sends task data to Django API via POST request.
 */

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("taskForm");
    if (!form) return;

    const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]")?.value;

    /**
     * Extract form values safely
     */
    const getFormData = () => ({
        title: document.querySelector("input[name=title]").value.trim(),
        description: document.querySelector("textarea[name=description]").value.trim(),
        due_date: document.querySelector("input[name=due_date]").value,
    });

    /**
     * Show user-friendly alerts
     */
    const notify = (msg) => alert(msg);

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const payload = getFormData();

        // Basic validation
        if (!payload.title || !payload.due_date) {
            notify("Title and Due Date are required!");
            return;
        }

        try {
            const response = await fetch("/api/create/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken,
                },
                body: JSON.stringify(payload),
            });

            if (response.ok) {
                notify("Task created successfully!");
                window.location.href = "/";
            } else {
                const errorData = await response.json().catch(() => ({}));
                notify(errorData.error || "Failed to create task.");
            }

        } catch (error) {
            console.error("Request failed:", error);
            notify("Network error occurred. Please try again.");
        }
    });
});
