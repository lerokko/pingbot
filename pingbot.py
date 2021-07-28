# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from pythonping import ping

response_list_US_EAST = ping('dynamodb.us-east-1.amazonaws.com', size=61, count=5)
response_list_US_WEST = ping('dynamodb.us-west-1.amazonaws.com', size=61, count=5)
response_list_EU_NORTH = ping('hel.icmp.hetzner.com', size=61, count=5)
response_list_EU_SOUTH = ping('ftp.pt.debian.org', size=61, count=5)
response_list_INDIA = ping('telecomepc.in', size=61, count=5)
response_list_TAIWAN = ping('ftp.tw.debian.org', size=61, count=5)
response_list_BRAZIL = ping('ftp.br.debian.org', size=61, count=5)
response_list_AUS = ping('speedtest.syd1.linode.com', size=61, count=5)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='serverping')
async def create_post(ctx):
	await ctx.send(
	'*Pinging some servers all around the world... (gimme a moment)*'
	)
	response_list_US_EAST = ping('dynamodb.us-east-1.amazonaws.com', size=61, count=5)
	response_list_US_WEST = ping('dynamodb.us-west-1.amazonaws.com', size=61, count=5)
	response_list_EU_NORTH = ping('hel.icmp.hetzner.com', size=61, count=5)
	response_list_EU_SOUTH = ping('ftp.pt.debian.org', size=61, count=5)
	response_list_INDIA = ping('telecomepc.in', size=61, count=5)
	response_list_TAIWAN = ping('ftp.tw.debian.org', size=61, count=5)
	response_list_BRAZIL = ping('ftp.br.debian.org', size=61, count=5)
	response_list_AUS = ping('speedtest.syd1.linode.com', size=61, count=5)
	await ctx.send(
	'```'
	'Ping to US_EAST is:     '+ str(response_list_US_EAST.rtt_avg_ms)+ 'ms\n'
	'Ping to US_WEST is:     '+ str(response_list_US_WEST.rtt_avg_ms)+ 'ms\n'
	'Ping to EU_NORTH is:    '+ str(response_list_EU_NORTH.rtt_avg_ms)+ 'ms\n'
	'Ping to EU_SOUTH is:    '+ str(response_list_EU_SOUTH.rtt_avg_ms)+ 'ms\n'
	'Ping to INDIA is:       '+ str(response_list_INDIA.rtt_avg_ms)+ 'ms\n'
	'Ping to TAIWAN is:      '+ str(response_list_TAIWAN.rtt_avg_ms)+ 'ms\n'
	'Ping to BRAZIL is:      '+ str(response_list_BRAZIL.rtt_avg_ms)+ 'ms\n'
	'Ping to AUSTRALIA is:   '+ str(response_list_AUS.rtt_avg_ms)+ 'ms\n'
	'```'
	)

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.errors.CheckFailure):
		await ctx.send('You do not have the requirements to execute this command.')

bot.run(TOKEN)
