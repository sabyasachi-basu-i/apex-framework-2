# Use official Node LTS
FROM node:18-slim

WORKDIR /app

# Install dependencies
COPY package.json package-lock.json* ./
RUN npm install

# Copy all files
COPY . .

# Accept build arguments for service URLs
ARG NEXT_PUBLIC_INTELLIGENCE_URL=http://intelligence:8001
ARG NEXT_PUBLIC_INTEGRATION_URL=http://integration:8002
ARG NEXT_PUBLIC_ORCHESTRATION_URL=http://orchestration:8003
ARG NEXT_PUBLIC_GOVERNANCE_URL=http://governance:8004
ARG NEXT_PUBLIC_CONFIG_PATH=/config

# Set environment variables from build args so Next.js can use them during build
ENV NEXT_PUBLIC_INTELLIGENCE_URL=$NEXT_PUBLIC_INTELLIGENCE_URL
ENV NEXT_PUBLIC_INTEGRATION_URL=$NEXT_PUBLIC_INTEGRATION_URL
ENV NEXT_PUBLIC_ORCHESTRATION_URL=$NEXT_PUBLIC_ORCHESTRATION_URL
ENV NEXT_PUBLIC_GOVERNANCE_URL=$NEXT_PUBLIC_GOVERNANCE_URL
ENV NEXT_PUBLIC_CONFIG_PATH=$NEXT_PUBLIC_CONFIG_PATH

# Build Next.js app with environment variables available
RUN npm run build

# Expose Next.js port
EXPOSE 3000

# Run production build
CMD ["npm", "start"]
