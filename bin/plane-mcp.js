#!/usr/bin/env node

import { spawn } from 'child_process';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const projectRoot = join(__dirname, '..');

// Check if uv is installed
function checkUv() {
  return new Promise((resolve) => {
    const uvCheck = spawn('uv', ['--version'], { stdio: 'ignore' });
    uvCheck.on('close', (code) => {
      resolve(code === 0);
    });
  });
}

// Main function
async function main() {
  // Check for uv installation
  const hasUv = await checkUv();
  
  if (!hasUv) {
    console.error('Error: uv is not installed.');
    console.error('');
    console.error('Install uv using one of these methods:');
    console.error('');
    console.error('macOS/Linux:');
    console.error('  curl -LsSf https://astral.sh/uv/install.sh | sh');
    console.error('');
    console.error('Windows (PowerShell):');
    console.error('  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"');
    console.error('');
    console.error('Or visit: https://docs.astral.sh/uv/getting-started/installation/');
    process.exit(1);
  }

  // Pass through all environment variables
  const env = {
    ...process.env,
    // Ensure PYTHONUNBUFFERED for real-time output
    PYTHONUNBUFFERED: '1',
  };

  // Run the MCP server using uv
  const child = spawn('uv', ['run', 'plane-mcp'], {
    cwd: projectRoot,
    stdio: 'inherit',
    env,
    shell: process.platform === 'win32' // Use shell on Windows for better compatibility
  });

  // Handle exit
  child.on('exit', (code, signal) => {
    if (signal) {
      process.kill(process.pid, signal);
    } else {
      process.exit(code || 0);
    }
  });

  // Handle termination signals
  process.on('SIGTERM', () => child.kill('SIGTERM'));
  process.on('SIGINT', () => child.kill('SIGINT'));
}

main().catch((error) => {
  console.error('Error starting plane-mcp:', error.message);
  process.exit(1);
});
