FROM node

WORKDIR /app

# RUN npx create-next-app --help
# RUN npx create-next-app . --ts --tailwind --eslint --app --src-dir --import-alias "@/*" --use-npm

COPY . .
RUN npm install

CMD ["npm", "run", "dev"]