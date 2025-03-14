/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useRef, onMounted } from "@odoo/owl";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { Component } from "@odoo/owl";
import { loadJS } from "@web/core/assets";

/**
 * Department Progress Widget
 * Displays progress bars for each department
 */
export class DepartmentProgressWidget extends Component {
    static template = "multi_dept_project.DepartmentProgress";
    static props = {
        ...standardFieldProps,
    };
    
    setup() {
        this.progressRef = useRef("progress");
        
        onMounted(() => {
            this.renderProgress();
        });
    }
    
    renderProgress() {
        if (!this.props.value) return;
        
        const progressData = JSON.parse(this.props.value);
        const progressContainer = this.progressRef.el;
        
        if (progressContainer && progressData) {
            progressContainer.innerHTML = '';
            
            Object.keys(progressData).forEach(deptName => {
                const dept = progressData[deptName];
                
                // Create department container
                const deptDiv = document.createElement('div');
                deptDiv.className = 'dept-progress mb-3';
                
                // Department name and stats
                const header = document.createElement('div');
                header.className = 'd-flex justify-content-between align-items-center mb-1';
                
                const nameSpan = document.createElement('span');
                nameSpan.className = 'fw-bold';
                nameSpan.textContent = deptName;
                
                const statsSpan = document.createElement('span');
                statsSpan.className = 'text-muted small';
                statsSpan.textContent = `${dept.done}/${dept.total} tasks`;
                
                header.appendChild(nameSpan);
                header.appendChild(statsSpan);
                
                // Progress bar
                const progressDiv = document.createElement('div');
                progressDiv.className = 'progress';
                
                const progressBar = document.createElement('div');
                progressBar.className = 'progress-bar';
                progressBar.style.width = `${dept.progress}%`;
                progressBar.textContent = `${Math.round(dept.progress)}%`;
                
                // Set color based on progress
                if (dept.progress < 30) {
                    progressBar.classList.add('bg-danger');
                } else if (dept.progress < 70) {
                    progressBar.classList.add('bg-warning');
                } else {
                    progressBar.classList.add('bg-success');
                }
                
                progressDiv.appendChild(progressBar);
                
                // Assemble full element
                deptDiv.appendChild(header);
                deptDiv.appendChild(progressDiv);
                
                progressContainer.appendChild(deptDiv);
            });
        }
    }
}

/**
 * Department Progress Chart
 * Chart.js visualization for department progress
 */
export class DepartmentProgressChart extends Component {
    static template = "multi_dept_project.DepartmentProgressChart";
    static props = {
        ...standardFieldProps,
    };
    
    setup() {
        this.chartRef = useRef("chart");
        this.chart = null;
        
        onMounted(async () => {
            await loadJS("/web/static/lib/Chart/Chart.js");
            this.renderChart();
        });
    }
    
    renderChart() {
        if (!this.props.value || !window.Chart) return;
        
        try {
            const chartData = JSON.parse(this.props.value);
            const ctx = this.chartRef.el.getContext('2d');
            
            // Destroy previous chart if it exists
            if (this.chart) {
                this.chart.destroy();
            }
            
            this.chart = new window.Chart(ctx, {
                type: 'bar',
                data: {
                    labels: chartData.labels,
                    datasets: chartData.datasets
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        } catch (error) {
            console.error('Error rendering chart:', error);
        }
    }
    
    willUnmount() {
        if (this.chart) {
            this.chart.destroy();
        }
    }
}

/**
 * Task Analysis Chart Widget
 */
export class TaskAnalysisChart extends Component {
    static template = "multi_dept_project.TaskAnalysisChart";
    static props = {
        ...standardFieldProps,
    };
    
    setup() {
        this.chartRef = useRef("chart");
        this.chart = null;
        
        onMounted(async () => {
            await loadJS("/web/static/lib/Chart/Chart.js");
            this.renderChart();
        });
    }
    
    renderChart() {
        if (!this.props.value || !window.Chart) return;
        
        try {
            const chartData = JSON.parse(this.props.value);
            const ctx = this.chartRef.el.getContext('2d');
            
            // Destroy previous chart if it exists
            if (this.chart) {
                this.chart.destroy();
            }
            
            this.chart = new window.Chart(ctx, {
                type: 'bar',
                data: chartData,
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        } catch (error) {
            console.error('Error rendering analysis chart:', error);
        }
    }
    
    willUnmount() {
        if (this.chart) {
            this.chart.destroy();
        }
    }
}

/**
 * Task Analysis Result Widget
 */
export class TaskAnalysisResult extends Component {
    static template = "multi_dept_project.TaskAnalysisResult";
    static props = {
        ...standardFieldProps,
    };
    
    setup() {
        this.resultRef = useRef("result");
        
        onMounted(() => {
            this.renderResult();
        });
    }
    
    renderResult() {
        if (!this.props.value) return;
        
        try {
            const analysisData = JSON.parse(this.props.value);
            const resultContainer = this.resultRef.el;
            
            if (resultContainer && analysisData) {
                resultContainer.innerHTML = '';
                
                // Summary section
                const summary = analysisData.summary;
                const summaryDiv = document.createElement('div');
                summaryDiv.className = 'summary-section mb-4 p-3 border rounded';
                
                const summaryTitle = document.createElement('h5');
                summaryTitle.textContent = 'Summary';
                summaryTitle.className = 'mb-3';
                
                const summaryStats = document.createElement('div');
                summaryStats.className = 'row';
                
                // Summary stats cards
                const createStatCard = (title, value, suffix = '', colorClass = 'primary') => {
                    const col = document.createElement('div');
                    col.className = 'col-md-3 col-6 mb-2';
                    
                    const card = document.createElement('div');
                    card.className = 'card h-100';
                    
                    const cardBody = document.createElement('div');
                    cardBody.className = 'card-body p-2 text-center';
                    
                    const cardTitle = document.createElement('h6');
                    cardTitle.className = 'card-title m-0 text-muted small';
                    cardTitle.textContent = title;
                    
                    const cardValue = document.createElement('div');
                    cardValue.className = `fs-4 text-${colorClass}`;
                    cardValue.textContent = `${value}${suffix}`;
                    
                    cardBody.appendChild(cardTitle);
                    cardBody.appendChild(cardValue);
                    card.appendChild(cardBody);
                    col.appendChild(card);
                    
                    return col;
                };
                
                summaryStats.appendChild(createStatCard('Total Tasks', summary.total_tasks));
                summaryStats.appendChild(createStatCard('Completed', summary.completed_tasks));
                summaryStats.appendChild(createStatCard('Completion Rate', Math.round(summary.completion_rate), '%', 'success'));
                summaryStats.appendChild(createStatCard('Bottlenecks', summary.bottlenecks_count, '', 'danger'));
                
                summaryDiv.appendChild(summaryTitle);
                summaryDiv.appendChild(summaryStats);
                resultContainer.appendChild(summaryDiv);
                
                // Departments section
                if (analysisData.departments && analysisData.departments.length > 0) {
                    const deptsDiv = document.createElement('div');
                    deptsDiv.className = 'departments-section mt-4';
                    
                    const deptsTitle = document.createElement('h5');
                    deptsTitle.textContent = 'Department Analysis';
                    deptsTitle.className = 'mb-3';
                    
                    const table = document.createElement('table');
                    table.className = 'table table-sm table-hover';
                    
                    // Table header
                    const thead = document.createElement('thead');
                    const headerRow = document.createElement('tr');
                    
                    ['Department', 'Tasks', 'Completed', 'Rate', 'Overdue', 'Bottlenecks', 'Avg Delay'].forEach(text => {
                        const th = document.createElement('th');
                        th.textContent = text;
                        headerRow.appendChild(th);
                    });
                    
                    thead.appendChild(headerRow);
                    table.appendChild(thead);
                    
                    // Table body
                    const tbody = document.createElement('tbody');
                    
                    analysisData.departments.forEach(dept => {
                        const row = document.createElement('tr');
                        
                        // Department name
                        const nameCell = document.createElement('td');
                        nameCell.className = 'fw-bold';
                        nameCell.textContent = dept.name;
                        row.appendChild(nameCell);
                        
                        // Total tasks
                        const totalCell = document.createElement('td');
                        totalCell.textContent = dept.total;
                        row.appendChild(totalCell);
                        
                        // Completed tasks
                        const completedCell = document.createElement('td');
                        completedCell.textContent = dept.completed;
                        row.appendChild(completedCell);
                        
                        // Completion rate
                        const rateCell = document.createElement('td');
                        rateCell.textContent = `${Math.round(dept.completion_rate)}%`;
                        if (dept.completion_rate < 30) {
                            rateCell.className = 'text-danger';
                        } else if (dept.completion_rate > 70) {
                            rateCell.className = 'text-success';
                        }
                        row.appendChild(rateCell);
                        
                        // Overdue tasks
                        const overdueCell = document.createElement('td');
                        overdueCell.textContent = dept.overdue;
                        if (dept.overdue > 0) {
                            overdueCell.className = 'text-danger';
                        }
                        row.appendChild(overdueCell);

                                                // Bottlenecks
                                                const bottleneckCell = document.createElement('td');
                                                bottleneckCell.textContent = dept.bottlenecks;
                                                if (dept.bottlenecks > 0) {
                                                    bottleneckCell.className = 'text-danger';
                                                }
                                                row.appendChild(bottleneckCell);
                                                
                                                // Average delay
                                                const delayCell = document.createElement('td');
                                                delayCell.textContent = dept.avg_delay > 0 ? `${dept.avg_delay} days` : '-';
                                                if (dept.avg_delay > 2) {
                                                    delayCell.className = 'text-danger';
                                                }
                                                row.appendChild(delayCell);
                                                
                                                tbody.appendChild(row);
                                            });
                                            
                                            table.appendChild(tbody);
                                            
                                            deptsDiv.appendChild(deptsTitle);
                                            deptsDiv.appendChild(table);
                                            resultContainer.appendChild(deptsDiv);
                                        }
                                    }
                                } catch (error) {
                                    console.error('Error rendering analysis result:', error);
                                }
                            }
                        }
                        
                        // Register widgets
                        registry.category("fields").add("department_progress_widget", DepartmentProgressWidget);
                        registry.category("fields").add("department_progress_chart", DepartmentProgressChart);
                        registry.category("fields").add("task_analysis_chart", TaskAnalysisChart);
                        registry.category("fields").add("task_analysis_result", TaskAnalysisResult);