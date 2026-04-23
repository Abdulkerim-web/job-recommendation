% =====================
% JOB RECOMMENDATION SYSTEM
% Using Prolog for rule-based recommendation
% =====================

% =====================
% JOB FACTS
% =====================
job('Data Scientist', 'python').
job('Data Scientist', 'machine learning').
job('Data Scientist', 'statistics').
job('Software Engineer', 'java').
job('Software Engineer', 'python').
job('Software Engineer', 'sql').
job('Data Analyst', 'excel').
job('Data Analyst', 'sql').
job('Data Analyst', 'python').
job('Marketing Manager', 'marketing').
job('Marketing Manager', 'social media').
job('Marketing Manager', 'analytics').
job('Product Manager', 'product management').
job('Product Manager', 'agile').
job('Product Manager', 'communication').
job('Web Developer', 'html').
job('Web Developer', 'css').
job('Web Developer', 'javascript').
job('DevOps Engineer', 'docker').
job('DevOps Engineer', 'kubernetes').
job('DevOps Engineer', 'aws').
job('UX Designer', 'figma').
job('UX Designer', 'sketch').
job('UX Designer', 'user research').
job('Financial Analyst', 'excel').
job('Financial Analyst', 'finance').
job('Financial Analyst', 'modeling').
job('HR Specialist', 'hr').
job('HR Specialist', 'recruitment').
job('HR Specialist', 'employee relations').
job('Business Analyst', 'business analysis').
job('Business Analyst', 'excel').
job('Business Analyst', 'communication').
job('Quality Assurance Engineer', 'testing').
job('Quality Assurance Engineer', 'automation').
job('Quality Assurance Engineer', 'selenium').
job('Customer Support Specialist', 'customer service').
job('Customer Support Specialist', 'communication').
job('Customer Support Specialist', 'troubleshooting').
job('Graphic Designer', 'photoshop').
job('Graphic Designer', 'illustrator').
job('Graphic Designer', 'creativity').
job('Content Writer', 'writing').
job('Content Writer', 'seo').
job('Content Writer', 'research').
job('Sales Representative', 'sales').
job('Sales Representative', 'negotiation').
job('Sales Representative', 'communication').
job('Social Media Manager', 'social media').
job('Social Media Manager', 'content creation').
job('Social Media Manager', 'analytics').
job('IT Support Technician', 'troubleshooting').
job('IT Support Technician', 'networking').
job('IT Support Technician', 'customer service').
job('Cybersecurity Analyst', 'security').
job('Cybersecurity Analyst', 'risk assessment').
job('Cybersecurity Analyst', 'incident response').
job('Database Administrator', 'sql').
job('Database Administrator', 'database administration').
job('Database Administrator', 'performance tuning').
job('Network Engineer', 'networking').
job('Network Engineer', 'routing').
job('Network Engineer', 'switching').
job('Operations Manager', 'operations').
job('Operations Manager', 'planning').
job('Operations Manager', 'leadership').
job('Recruitment Coordinator', 'recruiting').
job('Recruitment Coordinator', 'communication').
job('Recruitment Coordinator', 'interviewing').
job('Training Specialist', 'training').
job('Training Specialist', 'facilitation').
job('Training Specialist', 'documentation').
job('Legal Assistant', 'legal research').
job('Legal Assistant', 'communication').
job('Legal Assistant', 'organization').
job('Healthcare Coordinator', 'healthcare').
job('Healthcare Coordinator', 'coordination').
job('Healthcare Coordinator', 'communication').
job('Data Engineer', 'python').
job('Data Engineer', 'sql').
job('Data Engineer', 'etl').
job('Search Engine Optimization Specialist', 'seo').
job('Search Engine Optimization Specialist', 'analytics').
job('Search Engine Optimization Specialist', 'content').
job('Mobile App Developer', 'swift').
job('Mobile App Developer', 'kotlin').
job('Mobile App Developer', 'react native').
job('Project Coordinator', 'project coordination').
job('Project Coordinator', 'communication').
job('Project Coordinator', 'scheduling').
job('Event Planner', 'event planning').
job('Event Planner', 'coordination').
job('Event Planner', 'budgeting').
job('Supply Chain Analyst', 'supply chain').
job('Supply Chain Analyst', 'analytics').
job('Supply Chain Analyst', 'planning').
job('Technical Writer', 'technical writing').
job('Technical Writer', 'documentation').
job('Technical Writer', 'communication').
job('Training Manager', 'training').
job('Training Manager', 'leadership').
job('Training Manager', 'curriculum design').
job('E-commerce Specialist', 'ecommerce').
job('E-commerce Specialist', 'marketing').
job('E-commerce Specialist', 'analytics').
job('Research Analyst', 'research').
job('Research Analyst', 'analysis').
job('Research Analyst', 'reporting').
job('Business Development Manager', 'business development').
job('Business Development Manager', 'sales').
job('Business Development Manager', 'networking').
job('Customer Success Manager', 'customer success').
job('Customer Success Manager', 'relationship management').
job('Maintenance Technician', 'maintenance').
job('Maintenance Technician', 'repair').
job('Maintenance Technician', 'troubleshooting').
job('Executive Assistant', 'administrative').
job('Executive Assistant', 'organization').
job('Executive Assistant', 'communication').
job('Compliance Officer', 'compliance').
job('Compliance Officer', 'auditing').
job('Compliance Officer', 'reporting').

% =====================
% USER FACTS
% =====================
user_skill(1, 'python').
user_skill(1, 'machine learning').
user_skill(1, 'statistics').
user_skill(2, 'java').
user_skill(2, 'sql').
user_skill(2, 'javascript').
user_skill(3, 'excel').
user_skill(3, 'sql').
user_skill(3, 'marketing').
user_skill(4, 'html').
user_skill(4, 'css').
user_skill(4, 'javascript').
user_skill(5, 'finance').
user_skill(5, 'excel').
user_skill(5, 'modeling').
user_skill(6, 'hr').
user_skill(6, 'communication').
user_skill(6, 'recruitment').
user_skill(7, 'figma').
user_skill(7, 'user research').
user_skill(7, 'design').
user_skill(8, 'docker').
user_skill(8, 'aws').
user_skill(8, 'python').
user_skill(9, 'product management').
user_skill(9, 'agile').
user_skill(10, 'python').
user_skill(10, 'sql').
user_skill(10, 'analytics').

% =====================
% RULES
% =====================
recommend(User, Job) :- user_skill(User, Skill), job(Job, Skill).

% Advanced rules
matches_category(User, Category) :- user_skill(User, Skill), job(Job, Skill), job_category(Job, Category).
job_category(Job, Category) :- job(Job, _), category(Job, Category).

% Query examples:
% recommend(1, Job).
% matches_category(1, Category).
