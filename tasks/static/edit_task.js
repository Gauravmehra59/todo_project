/**
 * Edit Task Page Script
 * Loads task details, fills the form, and updates the task on submit.
 */

document.addEventListener("DOMContentLoaded", async () => {
    const form = document.getElementById("editForm");
    if (!form) return;

    // Extract ID from URL: /edit/5/
    const taskId = window.location.pathname.split("/").filter(Boolean).pop();

    /**
     * Fetch JSON safely
     */
    const fetchJSON = async (url, options = {}) => {
        try {
            const res = await fetch(url, options);
            const data = await res.json().catch(() => ({}));
            return { ok: res.ok, data };
        } catch (err) {
            console.error("Network error:", err);
            return { ok: false, data: { error: "Network error" } };
        }
    };

    /**
     * Fill form with task data
     */
    const loadTask = async () => {
        const { ok, data } = await fetchJSON(`/api/detail/${taskId}/`);

        if (!ok) {
            alert(data.error || "Failed to load task");
            return;
        }

        document.getElementById("title").value = data.title || "";
        document.getElementById("description").value = data.description || "";
        document.getElementById("due_date").value = data.due_date || "";
        document.getElementById("status").value = data.status || "pending";
    };

    await loadTask();

    /**
     * Collect form fields
     */
    const getPayload = () => ({
        title: document.getElementById("title").value.trim(),
        description: document.getElementById("description").value.trim(),
        due_date: document.getElementById("due_date").value,
        status: document.getElementById("status").value
    });

    /**
     * Form submit handler
     */
    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const payload = getPayload();

        if (!payload.title || !payload.due_date) {
            alert("Title and Due Date are required!");
            return;
        }

        const { ok, data } = await fetchJSON(`/api/update/${taskId}/`, {
            method: "PATCH",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
        });

        if (ok) {
            alert("Task updated successfully!");
            window.location.href = "/";
        } else {
            alert(data.error || "Error updating task");
        }
    });
});
