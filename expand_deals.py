#!/usr/bin/env python3
"""
Script để bổ sung thêm 50 deals mới cho nền tảng DealsVN
"""

import json
import random
from datetime import datetime, timedelta

def load_existing_deals():
    """Load deals hiện tại từ file JSON"""
    with open('/workspace/dealsvn/public/data/deals.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_new_deals():
    """Tạo 50 deals mới với vendors và categories đa dạng"""
    
    # Categories và vendors mới
    vendors_data = [
        # Development & DevOps
        {"name": "GitLab", "category": "Development", "logo": "/images/gitlab-logo.png"},
        {"name": "JetBrains", "category": "Development", "logo": "/images/jetbrains-logo.png"},
        {"name": "Heroku", "category": "Development", "logo": "/images/heroku-logo.png"},
        {"name": "DigitalOcean", "category": "Development", "logo": "/images/digitalocean-logo.png"},
        {"name": "MongoDB", "category": "Development", "logo": "/images/mongodb-logo.png"},
        {"name": "Redis", "category": "Development", "logo": "/images/redis-logo.png"},
        {"name": "Vercel", "category": "Development", "logo": "/images/vercel-logo.png"},
        {"name": "Supabase", "category": "Development", "logo": "/images/supabase-logo.png"},
        
        # Design & Creative
        {"name": "Adobe Creative Suite", "category": "Design", "logo": "/images/adobe-logo.png"},
        {"name": "Sketch", "category": "Design", "logo": "/images/sketch-logo.png"},
        {"name": "InVision", "category": "Design", "logo": "/images/invision-logo.png"},
        {"name": "Framer", "category": "Design", "logo": "/images/framer-logo.png"},
        {"name": "Principle", "category": "Design", "logo": "/images/principle-logo.png"},
        {"name": "Zeplin", "category": "Design", "logo": "/images/zeplin-logo.png"},
        
        # Marketing & Sales
        {"name": "ConvertKit", "category": "Marketing", "logo": "/images/convertkit-logo.png"},
        {"name": "Klaviyo", "category": "Marketing", "logo": "/images/klaviyo-logo.png"},
        {"name": "Sendinblue", "category": "Marketing", "logo": "/images/sendinblue-logo.png"},
        {"name": "Pipedrive", "category": "Sales", "logo": "/images/pipedrive-logo.png"},
        {"name": "Freshsales", "category": "Sales", "logo": "/images/freshsales-logo.png"},
        {"name": "Close", "category": "Sales", "logo": "/images/close-logo.png"},
        {"name": "Outreach", "category": "Sales", "logo": "/images/outreach-logo.png"},
        
        # Analytics & Data
        {"name": "Mixpanel", "category": "Analytics", "logo": "/images/mixpanel-logo.png"},
        {"name": "Amplitude", "category": "Analytics", "logo": "/images/amplitude-logo.png"},
        {"name": "Segment", "category": "Analytics", "logo": "/images/segment-logo.png"},
        {"name": "Tableau", "category": "Analytics", "logo": "/images/tableau-logo.png"},
        {"name": "Looker", "category": "Analytics", "logo": "/images/looker-logo.png"},
        
        # Customer Support
        {"name": "Zendesk", "category": "Support", "logo": "/images/zendesk-logo.png"},
        {"name": "Freshdesk", "category": "Support", "logo": "/images/freshdesk-logo.png"},
        {"name": "Intercom", "category": "Support", "logo": "/images/intercom-logo.png"},
        {"name": "Help Scout", "category": "Support", "logo": "/images/helpscout-logo.png"},
        {"name": "Crisp", "category": "Support", "logo": "/images/crisp-logo.png"},
        
        # Productivity & Project Management
        {"name": "Monday.com", "category": "Productivity", "logo": "/images/monday-logo.png"},
        {"name": "ClickUp", "category": "Productivity", "logo": "/images/clickup-logo.png"},
        {"name": "Todoist", "category": "Productivity", "logo": "/images/todoist-logo.png"},
        {"name": "Trello", "category": "Productivity", "logo": "/images/trello-logo.png"},
        {"name": "Linear", "category": "Productivity", "logo": "/images/linear-logo.png"},
        
        # Finance & Accounting
        {"name": "QuickBooks", "category": "Finance", "logo": "/images/quickbooks-logo.png"},
        {"name": "Xero", "category": "Finance", "logo": "/images/xero-logo.png"},
        {"name": "FreshBooks", "category": "Finance", "logo": "/images/freshbooks-logo.png"},
        {"name": "Wave", "category": "Finance", "logo": "/images/wave-logo.png"},
        
        # HR & Recruitment
        {"name": "BambooHR", "category": "HR", "logo": "/images/bamboohr-logo.png"},
        {"name": "Workday", "category": "HR", "logo": "/images/workday-logo.png"},
        {"name": "Greenhouse", "category": "HR", "logo": "/images/greenhouse-logo.png"},
        {"name": "Lever", "category": "HR", "logo": "/images/lever-logo.png"},
        
        # Security
        {"name": "1Password", "category": "Security", "logo": "/images/1password-logo.png"},
        {"name": "LastPass", "category": "Security", "logo": "/images/lastpass-logo.png"},
        {"name": "Okta", "category": "Security", "logo": "/images/okta-logo.png"},
        {"name": "Auth0", "category": "Security", "logo": "/images/auth0-logo.png"},
        
        # Communication
        {"name": "Discord", "category": "Communication", "logo": "/images/discord-logo.png"},
        {"name": "Microsoft Teams", "category": "Communication", "logo": "/images/teams-logo.png"},
        {"name": "Calendly", "category": "Communication", "logo": "/images/calendly-logo.png"},
        {"name": "Jitsi", "category": "Communication", "logo": "/images/jitsi-logo.png"},
    ]

    # Templates cho descriptions và features
    deal_templates = {
        "Development": {
            "descriptions": [
                "Platform phát triển phần mềm chuyên nghiệp với tính năng collaboration mạnh mẽ",
                "Công cụ development hiện đại với CI/CD tích hợp sẵn",
                "IDE và tools development với AI-powered coding assistance",
                "Cloud hosting platform với auto-scaling và deployment dễ dàng",
                "Database-as-a-Service với performance cao và security tốt nhất"
            ],
            "features": [
                ["CI/CD pipeline tự động", "Git repositories unlimited", "Issue tracking", "Code review tools"],
                ["Auto-scaling infrastructure", "Global CDN", "SSL certificates miễn phí", "Monitoring 24/7"],
                ["IDE tích hợp AI", "Code completion thông minh", "Debugging advanced", "Plugin ecosystem"],
                ["Database clustering", "Automatic backups", "Security monitoring", "Performance analytics"],
                ["Container orchestration", "Load balancing", "Health checks", "Blue-green deployment"]
            ]
        },
        "Design": {
            "descriptions": [
                "Công cụ thiết kế UI/UX chuyên nghiệp với collaborative features",
                "Platform design system với component library mạnh mẽ",
                "Tool thiết kế vector với AI-powered design suggestions",
                "Prototyping platform với interactive animations",
                "Design handoff tool kết nối designers và developers"
            ],
            "features": [
                ["Vector editing nâng cao", "Real-time collaboration", "Version control", "Asset management"],
                ["Component libraries", "Design tokens", "Auto-layout", "Responsive design"],
                ["Interactive prototypes", "Animation timeline", "Gesture support", "Device preview"],
                ["Developer handoff", "Code export", "Specs auto-generation", "Asset optimization"],
                ["Brand guidelines", "Style guides", "Team permissions", "Project templates"]
            ]
        },
        "Marketing": {
            "descriptions": [
                "Email marketing platform với automation workflows tiên tiến",
                "Social media management tool với AI content suggestions",
                "SEO optimization platform với keyword research mạnh mẽ",
                "Marketing analytics với multi-channel attribution",
                "Content marketing platform với team collaboration"
            ],
            "features": [
                ["Email automation", "Segmentation thông minh", "A/B testing", "Analytics chi tiết"],
                ["Multi-platform posting", "Content calendar", "Social listening", "Engagement tracking"],
                ["Keyword research", "Competitor analysis", "Site audit", "Rank tracking"],
                ["Attribution modeling", "Conversion tracking", "ROI calculation", "Custom dashboards"],
                ["Content planning", "Editorial calendar", "Team workflows", "Performance metrics"]
            ]
        },
        "Analytics": {
            "descriptions": [
                "User analytics platform với behavioral insights sâu sắc",
                "Business intelligence tool với real-time dashboards",
                "Customer data platform với 360-degree view",
                "Event tracking system với custom metrics",
                "Data visualization platform với interactive charts"
            ],
            "features": [
                ["Event tracking", "User segmentation", "Funnel analysis", "Cohort studies"],
                ["Real-time dashboards", "Custom metrics", "Data alerts", "Automated reports"],
                ["Customer profiles", "Journey mapping", "Predictive analytics", "Machine learning"],
                ["Custom events", "API integration", "Data export", "Team collaboration"],
                ["Interactive charts", "Drill-down analysis", "Data storytelling", "Export options"]
            ]
        },
        "Support": {
            "descriptions": [
                "Customer support platform với AI-powered chatbot",
                "Help desk solution với ticket management hiệu quả",
                "Live chat software với real-time visitor monitoring",
                "Knowledge base platform với search intelligence",
                "Customer feedback tool với sentiment analysis"
            ],
            "features": [
                ["Ticket management", "Live chat", "Knowledge base", "Automation rules"],
                ["Multi-channel support", "SLA management", "Team collaboration", "Performance analytics"],
                ["AI chatbot", "Visitor tracking", "Proactive messaging", "Mobile optimization"],
                ["Search functionality", "Content management", "Analytics", "Multilingual support"],
                ["Survey tools", "Feedback collection", "Sentiment tracking", "Reporting"]
            ]
        }
    }

    new_deals = []
    deal_id_start = 21  # Start from ID 21 since there are ~20 existing deals
    
    for i, vendor_data in enumerate(vendors_data[:50]):  # Limit to 50 deals
        vendor = vendor_data["name"]
        category = vendor_data["category"]
        logo = vendor_data["logo"]
        
        # Get appropriate template based on category
        templates = deal_templates.get(category, deal_templates["Development"])
        description = random.choice(templates["descriptions"])
        features = random.choice(templates["features"])
        
        # Generate random pricing and deal details
        original_price = random.choice([99, 149, 199, 299, 399, 499, 599, 799, 999, 1199])
        deal_type = random.choice(["discount", "discount", "credit"])  # More discounts than credits
        
        if deal_type == "credit":
            discounted_price = 0
            discount_percentage = 100
            credit_amount = random.choice([100, 250, 500, 1000, 2000])
        else:
            discount_percentage = random.choice([20, 25, 30, 40, 50, 60, 75])
            discounted_price = int(original_price * (100 - discount_percentage) / 100)
            credit_amount = 0
        
        # Random premium/lifetime status
        is_premium = random.choice([True, False])
        is_lifetime = random.choice([False, False, True])  # Less lifetime deals
        
        # Random expiry date (30-365 days from now)
        days_to_expire = random.randint(30, 365)
        expiry_date = (datetime.now() + timedelta(days=days_to_expire)).strftime("%Y-%m-%d")
        
        # Random usage stats
        rating = round(random.uniform(4.2, 4.9), 1)
        users_count = random.randint(1000, 25000)
        claimed_count = random.randint(100, int(users_count * 0.3))
        
        deal = {
            "id": str(deal_id_start + i),
            "title": f"{vendor} - {description.split()[0:3]}.join(' ')",
            "vendor": vendor,
            "category": category,
            "description": description,
            "originalPrice": original_price,
            "discountedPrice": discounted_price,
            "discountPercentage": discount_percentage,
            "dealType": deal_type,
            "creditAmount": credit_amount,
            "isPremium": is_premium,
            "isLifetime": is_lifetime,
            "expiryDate": expiry_date,
            "features": features,
            "logo": logo,
            "rating": rating,
            "usersCount": users_count,
            "claimedCount": claimed_count
        }
        
        # Fix title formatting
        title_parts = description.split()[:3]
        if category == "Development":
            deal["title"] = f"{vendor} - Development Platform"
        elif category == "Design":
            deal["title"] = f"{vendor} - Design Tool Professional"
        elif category == "Marketing":
            deal["title"] = f"{vendor} - Marketing Automation"
        elif category == "Analytics":
            deal["title"] = f"{vendor} - Analytics Platform"
        elif category == "Support":
            deal["title"] = f"{vendor} - Customer Support"
        elif category == "Productivity":
            deal["title"] = f"{vendor} - Productivity Suite"
        elif category == "Finance":
            deal["title"] = f"{vendor} - Financial Management"
        elif category == "HR":
            deal["title"] = f"{vendor} - HR Management"
        elif category == "Security":
            deal["title"] = f"{vendor} - Security Solution"
        elif category == "Communication":
            deal["title"] = f"{vendor} - Communication Platform"
        else:
            deal["title"] = f"{vendor} - Business Solution"
        
        new_deals.append(deal)
    
    return new_deals

def update_deals_file():
    """Cập nhật file deals.json với 50 deals mới"""
    print("📥 Loading existing deals...")
    existing_deals = load_existing_deals()
    print(f"✅ Loaded {len(existing_deals)} existing deals")
    
    print("🔧 Generating 50 new deals...")
    new_deals = generate_new_deals()
    print(f"✅ Generated {len(new_deals)} new deals")
    
    # Combine existing and new deals
    all_deals = existing_deals + new_deals
    print(f"📊 Total deals: {len(all_deals)}")
    
    # Save to both public and dist directories
    public_path = '/workspace/dealsvn/public/data/deals.json'
    dist_path = '/workspace/dealsvn/dist/data/deals.json'
    
    with open(public_path, 'w', encoding='utf-8') as f:
        json.dump(all_deals, f, ensure_ascii=False, indent=2)
    print(f"✅ Updated {public_path}")
    
    with open(dist_path, 'w', encoding='utf-8') as f:
        json.dump(all_deals, f, ensure_ascii=False, indent=2)
    print(f"✅ Updated {dist_path}")
    
    return len(all_deals)

if __name__ == "__main__":
    print("🚀 Bắt đầu bổ sung 50 deals mới cho DealsVN...")
    total_deals = update_deals_file()
    print(f"🎉 Hoàn thành! Tổng cộng hiện có {total_deals} deals trong hệ thống")
