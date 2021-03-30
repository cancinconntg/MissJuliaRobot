#    MissJuliaRobot (A Telegram Bot Project)
#    Copyright (C) 2019-2021 Julia (https://t.me/MissJulia_Robot)

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, in version 3 of the License.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see < https://www.gnu.org/licenses/agpl-3.0.en.html/ >.


from sys import argv, exit
from julia import tbot, ubot
from julia import TOKEN
import asyncio

# IDK WHY IT'S SO IMPORTANT, JUST DON'T REMOVE THIS
import julia.events

try:
    tbot.start(bot_token=TOKEN)
except Exception:
    print("Network Error/INVALID TOKEN !")
    exit(1)

# USING LONG POLLING
async def long_polling():
    await tbot.catch_up()
    await ubot.catch_up()


if len(argv) not in (1, 3, 4):
    tbot.disconnect()
else:
    asyncio.run(long_polling())
    tbot.run_until_disconnected()
