#!/usr/bin/env node

import { spawn } from 'child_process';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const projectRoot = join(__dirname, '..');

console.log('📦 Installing plane-mcp Python dependencies...');
console.log('');

// Check if uv is installed
function checkUv() {
  return new Promise((resolve) => {
    const uvCheck = spawn('uv', ['--version'], { stdio: 'pipe' });
    let version = '';
    uvCheck.stdout.on('data', (data) => {
      version += data.toString();
    });
    uvCheck.on('close', (code) => {
      if (code === 0) {
        console.log(`✅ Found uv: ${version.trim()}`);
      }
      resolve(code === 0);
    });
  });
}

// Install Python dependencies
function installDeps() {
  return new Promise((resolve, reject) => {
    console.log('📥 Installing Python packages with uv...');
    const uvSync = spawn('uv', ['sync'], {
      cwd: projectRoot,
      stdio: 'inherit',
      shell: process.platform === 'win32'
    });

    uvSync.on('close', (code) => {
      if (code === 0) {
        console.log('');
        console.log('✅ Dependencies installed successfully!');
        resolve();
      } else {
        reject(new Error(`uv sync failed with code ${code}`));
      }
    });
  });
}

async function main() {
  try {
    const hasUv = await checkUv();

    if (!hasUv) {
      console.log('⚠️  uv is not installed.');
      console.log('');
      console.log('🔧 Install uv using one of these methods:');
      console.log('');
      console.log('macOS/Linux:');
      console.log('  curl -LsSf https://astral.sh/uv/install.sh | sh');
      console.log('');
      console.log('Windows (PowerShell):');
      console.log('  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"');
      console.log('');
      console.log('Or visit: https://docs.astral.sh/uv/getting-started/installation/');
      console.log('');
      console.log('⏭️  Skipping Python dependency installation.');
      console.log('   You can install them later by running: uv sync');
      return;
    }

    await installDeps();

    console.log('');
    console.log('🎉 plane-mcp is ready to use!');
    console.log('');
    console.log('📝 Set your environment variables:');
    console.log('   PLANE_API_KEY - your Plane API key');
    console.log('   PLANE_WORKSPACE_SLUG - your workspace slug');
    console.log('   PLANE_API_HOST_URL - (optional) default: https://api.plane.so/');
    console.log('');
    console.log('🚀 Run: npx @mikey-semy/plane-mcp');

  } catch (error) {
    console.error('');
    console.error('❌ Installation failed:', error.message);
    console.error('');
    console.error('You can try installing manually:');
    console.error('  cd', projectRoot);
    console.error('  uv sync');
    process.exit(1);
  }
}

main();
