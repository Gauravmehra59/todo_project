/**
 * Task List Page Script
 * Loads tasks dynamically, handles delete & edit actions.
 */

document.addEventListener("DOMContentLoaded", async () => {
    const tableBody = document.getElementById("task-table-body");
    if (!tableBody) return;

    /**
     * Safe JSON fetch wrapper
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
     * Load tasks and render table rows
     */
    const loadTasks = async () => {
        const { ok, data } = await fetchJSON("/api/list/");

        if (!ok) {
            alert(data.error || "Failed to load tasks");
            return;
        }

        tableBody.innerHTML = "";

        if (!data.tasks || data.tasks.length === 0) {
            tableBody.innerHTML = `<tr><td colspan="6" style="text-align:center;">No tasks found</td></tr>`;
            return;
        }

        data.tasks.forEach((t) => {
            const tr = document.createElement("tr");
            tr.innerHTML = `
                <td>${t.id}</td>
                <td>${t.title}</td>
                <td>${t.description}</td>
                <td>${t.due_date}</td>
                <td>${t.status}</td>
                <td>
                    <button class="delete-btn" data-id="${t.id}">Delete</button>
                    <button class="edit-btn" data-id="${t.id}">Edit</button>
                </td>
            `;
            tableBody.appendChild(tr);
        });

        attachEvents();
    };

    /**
     * Bind delete & edit buttons
     */
    const attachEvents = () => {
        // DELETE Handler
        document.querySelectorAll(".delete-btn").forEach((btn) => {
            btn.addEventListener("click", async function () {
                const id = this.dataset.id;

                if (!confirm("Are you sure you want to delete?")) return;

                const { ok, data } = await fetchJSON(`/api/delete/${id}/`, {
                    method: "DELETE"
                });

                if (ok) {
                    alert("Task deleted successfully");
                    loadTasks(); // reload only table section, no full page reload
                } else {
                    alert(data.error || "Error deleting task");
                }
            });
        });

        // EDIT Handler
        document.querySelectorAll(".edit-btn").forEach((btn) => {
            btn.addEventListener("click", function () {
                const id = this.dataset.id;
                window.location.href = `/detail/${id}/`;
            });
        });
    };

    // Load tasks on page ready
    loadTasks();
});
