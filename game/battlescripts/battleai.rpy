init python:
    class BattleAI:
        def __init__(self):
            self.threattable = {} #cache to reduce calculation time

        def ShouldSwitch(self, user):
            if user.GetTrainer().Skill == 0 or IsBefore(10, 6, 2004):
                return None
            switchmovelist = []
            for move in user.GetMoves():
                if move.Name in ["Volt Switch", "U-turn", "Flip Turn", "Parting Shot", "Baton Pass", "Shed Tail", "Teleport", "Chilly Reception"]:
                    switchmovelist.append(move)
            if len(switchmovelist) == 0 and not CanSwitch(user, False):
                return None
            willswitch = None
            bestswitchvalue = 0
            for switch in user.GetTrainer().GetTeam():
                if switch.GetHealth() == 0 or switch in Battlers() or switch in SwappingInMon:
                    continue
                switchvalue = self.GetSwitchValue(user, switch)
                if switchvalue > bestswitchvalue:
                    bestswitchvalue = switchvalue
                    willswitch = switch

            if not willswitch:
                return None

            if len(switchmovelist) > 0:
                for target in RankTargets(user):
                    if not target[1] in switchmovelist:
                        continue
                    if not (target[1].Category == "Status" or self.CalcDamage(user, target[0], target[1])["maxDamage"] > 0):
                        continue

                    moverange = GetMoveRange(movechosen)
                    targets = GetTargets(user, moverange, True)
                    
                    if not (moverange in [Range.AllAdjacentFoes, Range.AllAdjacent, Range.AllAllies, Range.AllFoes, Range.All, Range.AllAlliesAndSelf] or len(targets) == 0):
                        if (target[0] != -1):
                            targets = [target[0]]
                        else:
                            targets = [random.choice(targets)]


                    return Action(0, user.GetStat(Stats.Speed), ActionTypes.Move, user.GetTrainer(), user, target[1], GetTrainers(targets), targets, Turn)

            if not CanSwitch(user, False):
                return None

            SwappingInMon.append(willswitch)
            return Action(6, user.GetStat(Stats.Speed), ActionTypes.Pokemon, user.GetTrainer(), user, None, [user.GetTrainer()], [willswitch], Turn)

        def MidTurnSwitch(self, user):
            self.threattable = {}
            willswitch = None
            bestswitchvalue = 0
            for switch in user.GetTrainer().GetTeam():
                if switch.GetHealth() == 0 or switch in Battlers():
                    continue
                switchvalue = self.GetSwitchValue(user, switch)
                if willswitch == None or switchvalue > bestswitchvalue:
                    bestswitchvalue = switchvalue
                    willswitch = switch

            return willswitch

        def GetSwitchValue(self, user, switch):
            if CustomSwitchBrain:
                switchScore = CustomSwitchBrain(user, switch)
            else:
                switchScore = 0
            if user.GetTrainer().Skill == 0:
                switchScore += random.random()
                return switchScore

            activeUserThreat = 1
            activeOpposingThreat = 1
            activeUserOutspeeds = True
            switchThreat = 1
            opposingThreat = 1
            switchOutspeeds = True
            for target in GetBattlers(user, True):
                if not target in GetTargets(user): #todo account for flying moves
                    continue
                opposingThreat += self.GetThreat(switch, target)["highestDamage"]
                switchThreat = max(self.GetThreat(target, switch)["highestDamage"], switchThreat)
                if target.GetStat(Stats.Speed) >= switch.GetStat(Stats.Speed):
                    switchOutspeeds = False
                if user.GetHealthPercentage() == 0:
                    activeUserThreat = 1
                    activeOpposingThreat = 100
                    activeUserOutspeeds = False
                    continue
                activeOpposingThreat += self.GetThreat(user, target)["highestDamage"]
                activeUserThreat = max(self.GetThreat(target, user)["highestDamage"], activeUserThreat)
                if target.GetStat(Stats.Speed) >= user.GetStat(Stats.Speed):
                    activeUserOutspeeds = False

            opposingThreat = min(opposingThreat, 100)
            activeOpposingThreat = min(activeOpposingThreat, 100)

            damagethreshold = math.ceil((100 - opposingThreat) / opposingThreat) if user.GetHealthPercentage() else math.ceil(100 / opposingThreat)
            if switchOutspeeds:
                damagethreshold += 1
            activeDamagethreshold = math.ceil(100 / activeOpposingThreat)
            if activeUserOutspeeds:
                activeDamagethreshold += 1
            hitsDifferential = (1 + math.floor(100/switchThreat)) / math.floor(100 / activeUserThreat)
            switchScore += damagethreshold - (activeDamagethreshold * hitsDifferential)
            switchScore += self.GetSwitchBonus(switch, opposingThreat, damagethreshold)
            switchScore += self.GetSwitchBonus(user, activeOpposingThreat, activeDamagethreshold)
            switchScore += (damagethreshold - activeDamagethreshold) * 0.5
            switchScore -= 1

            #discourage low skill from switching if the benefit is too small
            if user.GetTrainer().Skill < 3:
                switchScore -= 3 - user.GetTrainer().Skill
            #add variance to low skill switching
            if user.GetTrainer().Skill < 3:
                switchScore += user.GetTrainer().Skill * (math.ceil(random.random() * 3) - 2)

            # print(pokedexlookup(user.Id, DexMacros.Name), activeUserThreat, activeOpposingThreat)
            # print(pokedexlookup(switch.Id, DexMacros.Name), switchThreat, opposingThreat)
            # print(switchScore)

            return switchScore

        def GetSwitchBonus(self, user, threat, damagethreshold):
            switchScore = 0
            switchinScore = 0
            switchoutScore = 0
            activeScore = 0

            if user.HasAbility("Snow Warning") and not WeatherIs("snowy"):
                switchScore += 2
            if user.HasAbility("Drizzle") and not WeatherIs("rainy"):
                switchScore += 2
            if user.HasAbility("Sand Stream") and not WeatherIs("sandstorm"):
                switchScore += 2
            if user.HasAbility("Drought") and not WeatherIs("sunny"):
                switchScore += 2
            if user.HasAbility("Intimidate", False):
                switchScore += 1
            if user.HasAbility("Regenerator", False):
                switchScore += 1

            if user.HasStatus("drowsy"):
                switchoutScore += 3
            if user.HasStatus("infatuated"):
                switchoutScore += 2
            if user.HasStatus("seeded") and not user.HasAbility("Magic Guard", False):
                switchoutScore += 2
            if user.HasStatus("cursed") and not user.HasAbility("Magic Guard", False):
                switchoutScore += 3
            if user.GetStatusCount("perishing") == 1:
                switchoutScore += 5
            if not (user.HasAbility("Poison Heal", False) or user.HasAbility("Magic Guard", False)):
                switchoutScore += max(0, user.GetStatusCount("badly poisoned") - 2)
            if len([move for move in ["Volt Switch", "U-turn", "Flip Turn", "Parting Shot", "Baton Pass", "Shed Tail", "Teleport", "Chilly Reception"] if user.GetMoveByName(move)]) > 0:
                switchoutScore += 1

            switchScore += switchoutScore if user in Battlers() else switchinScore
            switchScore += -activeScore if user in Battlers() else activeScore

            return switchScore

        def GetThreat(self, user, target, percentagetotal = True): #returns targets threat on the user
            if not user == target:
                threattable = self.AssessThreat(user, target)
            else:
                maxthreat = 0
                for battler in GetBattlers(user, True):
                    threat = self.AssessThreat(user, battler)
                    if threat["highestDamage"] >= maxthreat:
                        threattable = threat

            maxhp = user.Stats[Stats.Health] if percentagetotal else user.Health
            newtable = {}
            for key, threat in threattable.items():
                newtable[key] = threat
                if key == "moves":
                    continue
                newtable[key] = max(min(100, threat * 100 / maxhp), 1)

            return newtable

        def AssessThreat(self, user, target):
            if not target in self.threattable:
                self.threattable[target] = {}
            if user in self.threattable[target]:
                return self.threattable[target][user]
            self.threattable[target][user] = {
                "highestDamage": 0,
                "physicalDamage": 0,
                "specialDamage": 0,
                "statusCount": 0,
                "moves": {}
            }

            key = "maxDamage" if user.GetTrainerType() == TrainerType.Enemy else "minDamage"

            for move in target.GetMoves():
                self.threattable[target][user]["moves"][move] = self.CalcDamage(target, user, move)
                damage = self.threattable[target][user]["moves"][move][key]
                if self.threattable[target][user]["moves"][move]["category"] == "Status":
                    self.threattable[target][user]["statusCount"] += 1
                    continue
                if damage > self.threattable[target][user]["highestDamage"]:
                    self.threattable[target][user]["highestDamage"] = damage
                    if damage > self.threattable[target][user]["physicalDamage"]:
                        self.threattable[target][user]["physicalDamage"] = damage
                    if damage > self.threattable[target][user]["specialDamage"]:
                        self.threattable[target][user]["specialDamage"] = damage
            return self.threattable[target][user]

        def CalcDamage(self, user, target, move):
            damagedictionary = {
                "minDamage": 0,
                "averageDamage": 0,
                "maxDamage": 0,
                "critDamage": 0,
                "category": move.Category
            }

            for key, damage in damagedictionary.items():
                originalkey = key
                damage = 0
                power = move.Power
                element = move.Type
                isSpecial = move.Category == "Special"

                iscrit=(key=="critdamage")
                typebonus=GetTypeBonus(move.Name, element, target, user)
                sheerforcebonus=True
                recklessbonus=user.HasAbility("Reckless", False)
                atebonus=False
                analyticbonus=target.GetStat(Stats.Speed) > user.GetStat(Stats.Speed)
                parentalbond=user.HasAbility("Parental Bond", False)
                contact=MakesContact(move)

                atkStat = Stats.SpecialAttack if isSpecial else Stats.Attack
                atkStatVal = user.GetStat(atkStat, ignorenegative=iscrit)
                if (move.Name != "Foul Play"):
                    if (user.GetStatChanges(atkStat) != 0 and target.HasAbility("Unaware", False)):
                        atkStatVal = user.GetStat(atkStat, ignorenegative=True, ignorepositive=True)
                else:
                    atkStatVal = target.GetStat(atkStat, ignorenegative=iscrit)

                defStat = Stats.SpecialDefense if isSpecial else Stats.Defense
                if (move.Name in ["Psyshock", "Psystrike"]):
                    defStat = Stats.Defense
                defStatVal = target.GetStat(defStat, ignorepositive=iscrit)
                if (target.GetStatChanges(defStat) != 0 and (user.HasAbility("Unaware", False) or move.Name in ["Chip Away", "Darkest Lariat"])):
                    defStatVal = target.GetStat(defStat, ignorenegative=True, ignorepositive=True)

                foreveralstab = False
                for fvl in user.GetForeverals():
                    if (element in lookupforeveraldata(fvl, FVLMacros.FVLTypeData)):
                        if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.AddSTAB 
                            or user.GetId() == 25.2 and lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.AddProficiency):
                            foreveralstab = True
                            break

                stabbonus = 1.5 if foreveralstab or user.HasType(element) or (user.GetTerastallized() != -1 and element == user.GetTeraType()) else 1.0
                stabbonus = 2.0 if (not user.IsTerad() and stabbonus == 1.5 and user.HasAbility("Adaptability", False)) or (user.IsTerad() and element == user.GetTeraType() and user.HasAbility("Adaptability", False)) else stabbonus
                stabbonus = 2.25 if (user.IsTerad() and user.HasAbility("Adaptability", False) and element == user.GetTeraType() and element in user.GetTypes(ignoreTera=True)) else stabbonus
                burnpenalty = 0.5 if (user.HasStatus("burned") and not isSpecial and not user.HasAbility("Guts", False)) else 1.0
                mudsportpenalty = 0.33 if element == "Electric" and BattlefieldExists("Mud Sport") else 1.0
                watersportpenalty = 0.33 if element == "Fire" and BattlefieldExists("Water Sport") else 1.0
                critbonus = 1.5 if iscrit else 1.0
                critbonus = 2.25 if iscrit and user.HasAbility("Sniper", False) else critbonus
                mistyterrainpenalty = 0.5 if element == "Dragon" and BattlefieldExists("Misty Terrain") and IsGrounded(target) else 1.0
                electricterrainbonus = 1.3 if element == "Electric" and BattlefieldExists("Electric Terrain") and IsGrounded(user) else 1.0
                grassyterrainbonus = 1.3 if element == "Grass" and BattlefieldExists("Grassy Terrain") and IsGrounded(user) else 1.0
                grassyterrainpenalty = 0.5 if move.Name in ["Magnitude", "Earthquake", "Bulldoze"] and BattlefieldExists("Grassy Terrain") and IsGrounded(target) else 1.0
                chargedbonus = 2.0 if element == "Electric" and user.HasStatus("charged") else 1.0
                steelworkerbonus = 1.5 if element == "Steel" and user.HasAbility("Steelworker", False) else 1.0
                ironfistbonus = 1.2 if IsPunchMove(move.Name) and user.HasAbility("Iron Fist", False) else 1.0
                sharpnessbonus = 1.5 if IsSliceMove(move.Name) and user.HasAbility("Sharpness", False) else 1.0
                blazebonus = 1.5 if element == "Fire" and user.GetHealthPercentage() <= 1.0/3.0 and user.HasAbility("Blaze", False) else 1.0
                torrentbonus = 1.5 if element == "Water" and user.GetHealthPercentage() <= 1.0/3.0 and user.HasAbility("Torrent", False) else 1.0
                overgrowbonus = 1.5 if element == "Grass" and user.GetHealthPercentage() <= 1.0/3.0 and user.HasAbility("Overgrow", False) else 1.0
                swarmbonus = 1.5 if element == "Bug" and user.GetHealthPercentage() <= 1.0/3.0 and user.HasAbility("Swarm", False) else 1.0
                tintedlensbonus = 2.0 if typebonus < 1 and user.HasAbility("Tinted Lens", False) else 1.0
                sheerforcebonus = 1.3 if sheerforcebonus and user.HasAbility("Sheer Force", False) else 1.0
                strongjawbonus = 1.5 if IsBiteMove(move.Name) and user.HasAbility("Strong Jaw", False) else 1.0
                recklessbonus = 1.2 if recklessbonus else 1.0
                flashfirebonus = 1.5 if element == "Fire" and user.HasStatus("aflame") and user.HasAbility("Flash Fire", False) else 1.0
                sandforcebonus = 1.3 if element in ["Rock", "Ground", "Steel"] and WeatherIs("sandstorm") and user.HasAbility("Sand Force", False) else 1.0
                thickfatpenalty = 0.5 if element in ["Ice", "Fire"] and target.HasAbility("Thick Fat", False) else 1.0
                defensecurlcombo = 2.0 if move.Name in ["Rollout", "Ice Ball"] and user.HasStatus(".curling") else 1.0
                technicianbonus = 1.5 if move.Power <= 60 and user.HasAbility("Technician", False) else 1.0
                stompbonus = 2.0 if move.Name in ["Stomp", "Body Slam", "Dragon Rush", "Steamroller", "Heat Crash", "Heavy Slam", "Flying Press", "Malicious Moonsault"] and target.HasStatus(".minimized") else 1.0
                helpinghandbonus = pow(1.5, user.GetStatusCount("helped"))
                dryskinbonus = 1.25 if element == "Fire" and target.HasAbility("Dry Skin", False) else 1.0
                screenspenalty = 0.67 if target.GetTrainer().Number >= 2 or (target.GetTrainerType() == TrainerType.Enemy and len(EnemyTrainers()) >= 2) or (target.GetTrainerType() != TrainerType.Enemy and len(FriendlyTrainers()) >= 2) else 0.5
                lightscreenpenalty = screenspenalty if isSpecial and EffectOnOwnField(target, "light screen") else 1.0
                reflectpenalty = screenspenalty if not isSpecial and EffectOnOwnField(target, "reflect") else 1.0
                auroraveilpenalty = screenspenalty if lightscreenpenalty + reflectpenalty == 2 and EffectOnOwnField(target, "aurora veil") else 1.0
                rivalrybonus = 1.25 if user.GetGender() == target.GetGender() and user.GetGender() != Genders.Unknown and user.HasAbility("Rivalry", False) else 1.0
                rivalrypenalty = 0.75 if user.GetGender() != target.GetGender() and user.GetGender() != Genders.Unknown and target.GetGender() != Genders.Unknown  and user.HasAbility("Rivalry", False) else 1.0
                sunbonus = 1.5 if WeatherIs("sunny") and element == "Fire" else 1.0
                sunpenalty = 0.5 if WeatherIs("sunny") and element == "Water" else 1.0
                rainbonus = 1.5 if WeatherIs("rainy") and element == "Water" else 1.0
                rainpenalty = 0.5 if WeatherIs("rainy") and element == "Fire" else 1.0
                toughclawsbonus = 1.3 if contact and user.HasAbility("Tough Claws", False) else 1.0
                atebonus = 1.2 if atebonus and user.HasAbility("Pixilate", False) else 1.0
                analyticbonus = 1.3 if analyticbonus and user.HasAbility("Analytic", False) else 1.0
                stakeoutbonus = 2.0 if target.GetTurnSwitchedIn() == Turn and user.HasAbility("Stakeout", False) else 1.0
                filterpenalty = 0.75 if typebonus > 1 and (target.HasAbility("Filter") or target.HasAbility("Solid Rock", False) or target.HasAbility("Prism Armor", False)) else 1.0
                punkrockbonus = 1.3 if IsSoundMove(move.Name) and user.HasAbility("Punk Rock", False) else 1.0
                punkrockpenalty = 0.5 if IsSoundMove(move.Name) and target.HasAbility("Punk Rock", False) else 1.0
                friendguardpenalty = 0.75 * GetFriendGuardCount(target)
                parentalbondpenalty = 1.25 if parentalbond else 1.0
                fluffypenalty = 0.5 if contact and target.HasAbility("Fluffy", False) else 1.0
                fluffybonus = 2.0 if element == "Fire" and target.HasAbility("Fluffy", False) else 1.0
                purifyingsaltpenalty = 0.5 if element == "Ghost" and target.HasAbility("Purifying Salt", False) else 1.0
                icescalespenalty = 0.5 if isSpecial and target.HasAbility("Ice Scales", False) else 1.0
                supremeoverlordbonus = user.GetStatusCount("reigning supreme") if user.GetStatusCount("reigning supreme") != 0 else 1.0
                waterbubblepenalty = 0.5 if element == "Fire" and target.HasAbility("Water Bubble", False) else 1.0
                waterbubblebonus = 2.0 if element == "Water" and user.HasAbility("Water Bubble", False) else 1.0
                vulnerablebonus = 2.0 if target.HasStatus("vulnerable") else 1.0
                powerspotbonus = 1.3 if AbilityOnOwnField(user, "Power Spot", True) else 1.0
                batterybonus = 1.3 if isSpecial and AbilityOnOwnField(user, "Battery", True) else 1.0
                steelyspiritbonus = pow(1.5, NumAbilityOnOwnField(user, "Steely Spirit")) if element == "Steel" else 1.0
                thricedeniedpenalty = 0.333 if target.HasAbility("Thrice Denied", False) else 1.0
                randomvariation = 0.85 if key == "mindamage" else (1.85/2 if key == "averagedamage" else 1)

                basepower = PokeRound(power * defensecurlcombo
                    * rivalrybonus * rivalrypenalty
                    * atebonus * ironfistbonus * recklessbonus
                    * sheerforcebonus * sandforcebonus * analyticbonus * toughclawsbonus
                    * punkrockbonus * technicianbonus * strongjawbonus * sharpnessbonus
                    * dryskinbonus * helpinghandbonus * chargedbonus
                    * mistyterrainpenalty * electricterrainbonus * grassyterrainbonus
                    * watersportpenalty * mudsportpenalty 
                    * supremeoverlordbonus * waterbubblebonus * powerspotbonus * batterybonus
                    * steelyspiritbonus)

                atkStatVal = PokeRound(atkStatVal
                    * overgrowbonus * blazebonus * torrentbonus * swarmbonus * flashfirebonus * steelworkerbonus
                    * stakeoutbonus * thickfatpenalty * purifyingsaltpenalty)

                atkStatVal = 1 if atkStatVal < 1 else atkStatVal

                basedamage = math.floor(math.floor(math.floor(2.0 * user.GetLevel() / 5.0 + 2) * basepower * atkStatVal / defStatVal) / 50.0) + 2
                basedamage = PokeRound(basedamage * parentalbondpenalty)
                basedamage = PokeRound(basedamage * sunbonus * sunpenalty * rainbonus * rainpenalty)
                basedamage = PokeRound(basedamage * critbonus)
                basedamage = math.floor(basedamage * randomvariation)
                basedamage = PokeRound(basedamage * stabbonus)
                basedamage = math.floor(basedamage * typebonus)
                basedamage = PokeRound(basedamage * burnpenalty)
                basedamage = PokeRound(basedamage * waterbubblepenalty)
                basedamage = PokeRound(basedamage * thricedeniedpenalty)

                damage = PokeRound(basedamage
                    * reflectpenalty * lightscreenpenalty * auroraveilpenalty
                    * tintedlensbonus * fluffypenalty * filterpenalty * fluffybonus 
                    * stompbonus * punkrockpenalty * icescalespenalty * vulnerablebonus)

                damage = 1 if damage <= 0 else damage

                damagedictionary[key] = damage

            return damagedictionary
