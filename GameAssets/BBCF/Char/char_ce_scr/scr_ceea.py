@State
def EMB_CE():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_CE.DIG', '')
        RenderLayer(5)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4278190335, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 10)
    ColorTransition(4294967295, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 79)


@State
def EMB_CE_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_CE.DIG', '')
        RenderLayer(5)
    sprite('null', 8)
    ColorForTransition(4278190080)
    ColorTransition(4294967295, 10)
    sprite('null', 8)
    ColorTransition(4286625023, 10)
    sprite('null', 8)
    ColorTransition(4278223103, 10)
    sprite('null', 8)
    ColorTransition(4278223103, 10)
    sprite('null', 79)


@State
def EMB_CE_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_CE.DIG', '')
        RenderLayer(5)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4294901760, 10)
    sprite('null', 10)
    ColorTransition(4294912040, 10)
    sprite('null', 10)
    ColorTransition(4294948020, 10)
    sprite('null', 10)
    ColorTransition(4294901760, 10)
    sprite('null', 79)


@Subroutine
def MV_ActReset():
    AttackDefaults_Projectile()
    AttackOff()
    AbsoluteY(0)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    EnableCollision(0)
    SetZVal(500)
    NoDamageAction(1)
    IgnoreScreenfreeze(1)
    AutoHitStopSending(1)
    Unknown23042()

    def upon_48():
        if not SLOT_4:
            Visibility(1)
            EndAttack()
        else:
            Visibility(0)

    def upon_EVERY_FRAME():
        TurnAround()
        if not SLOT_51:
            if SLOT_IsAirborne:
                PrivateFunction3(3, 0, 0, 25, 0)
            else:
                PrivateFunction3(3, -100000, 0, 25, 0)
        else:
            if SLOT_52 == 1:
                if SLOT_IsAirborne:
                    PrivateFunction3(3, 0, 0, 5, 0)
                else:
                    PrivateFunction3(3, -100000, 0, 5, 0)
            if SLOT_52 == 2:
                if SLOT_IsAirborne:
                    PrivateFunction3(3, 0, 0, 50, 0)
                else:
                    PrivateFunction3(3, -100000, 0, 50, 0)
            if SLOT_52 == 3:
                if SLOT_IsAirborne:
                    PrivateFunction3(3, 0, 0, 100, 0)
                else:
                    PrivateFunction3(3, -100000, 0, 100, 0)
            if SLOT_52 == 4:
                TeleportToObject(3)
    callSubroutine('MinervaSignalSetup')


@Subroutine
def MV_AtkInit():
    MoveAttributes(0, 1, 0, 0, 0)
    StrikeProjectileLevel(1)
    ProjectileLevel(0)
    HitAirUnblockable(3)
    AttackDirection(3)
    IgnorePauses(3)
    AttackOff()


@Subroutine
def MV_ChainAtkInit():
    if not SLOT_6:
        TeleportToObject(3)
        AddX(-100000)
    else:
        SLOT_51 = 1
        ObjectUpon24(23, 104, 3, 104)
        if SLOT_0 > 100000:
            CopyFromRightToLeft(23, 2, 56, 23, 2, 19)
            CopyFromRightToLeft(23, 2, 57, 3, 2, 19)
            if SLOT_57 > SLOT_56:
                TeleportToObject(3)
                ForceFaceSprite()
                AddX(100000)

    def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
        SLOT_51 = 1

    def upon_48():
        if SLOT_XDistanceFromFowardCorner < 200000:
            AddX(-50000)
        if SLOT_StateDuration == 2:
            SLOT_6 = 1
            clearUponHandler(48)


@State
def MinervaCreate():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        NoDamageAction(1)
        TeleportToObject(3)
        AddX(-360000)
        AbsoluteY(0)
        ShadowOffsetY(-75000)
        CreateDecalOn(1)

        def upon_EVERY_FRAME():
            TurnAround()
            physicsXImpulse(0)
            if not SLOT_4:
                Visibility(1)
            else:
                Visibility(0)
    sprite('null', 1)
    sprite('mv000_00', 100)
    enterState('MinervaStand')


@Subroutine
def MinervaSignalSetup():

    def upon_VALUE_RECEIVED():
        if SLOT_ReceivedValue == 100:
            SLOT_6 = 0
            PrivateFunction2('MinervaStand', 900)
        if SLOT_ReceivedValue == 112:
            SLOT_6 = 0
            PrivateFunction2('MinervaStandReaction', 1000)
        if SLOT_ReceivedValue == 101:
            SLOT_6 = 0
            PrivateFunction2('MinervaTurn', 1000)
        if SLOT_ReceivedValue == 102:
            SLOT_6 = 0
            PrivateFunction2('MinervaFWalk', 800)
        if SLOT_ReceivedValue == 103:
            SLOT_6 = 0
            PrivateFunction2('MinervaBWalk', 800)
        if SLOT_ReceivedValue == 110:
            SLOT_6 = 0
            PrivateFunction2('MinervaHold', 900)
        if SLOT_ReceivedValue == 111:
            SLOT_6 = 0
            PrivateFunction2('MinervaSlowHoming', 900)
        if SLOT_ReceivedValue == 300:
            PrivateFunction2('MinervaAtk5B', 1000)
        if SLOT_ReceivedValue == 301:
            PrivateFunction2('MinervaAtk5C', 1000)
        if SLOT_ReceivedValue == 310:
            PrivateFunction2('MinervaAtk2B', 1000)
        if SLOT_ReceivedValue == 311:
            PrivateFunction2('MinervaAtk2C', 1000)
        if SLOT_ReceivedValue == 312:
            PrivateFunction2('MinervaAtk3C', 1000)
        if SLOT_ReceivedValue == 320:
            PrivateFunction2('MinervaAtk6B', 1000)
        if SLOT_ReceivedValue == 321:
            PrivateFunction2('MinervaAtk6C', 1000)
        if SLOT_ReceivedValue == 330:
            SLOT_6 = 0
            PrivateFunction2('MinervaAtkAIR5B', 1000)
        if SLOT_ReceivedValue == 331:
            SLOT_6 = 0
            PrivateFunction2('MinervaAtkAIR5C', 1000)
        if SLOT_ReceivedValue == 400:
            PrivateFunction2('MinervaAtkShot', 1000)
        if SLOT_ReceivedValue == 401:
            SLOT_6 = 0
            PrivateFunction2('MinervaAtkAirAssault', 1000)
        if SLOT_ReceivedValue == 402:
            PrivateFunction2('MinervaAtkUltimateShot', 1000)
        if SLOT_ReceivedValue == 403:
            PrivateFunction2('MinervaAtkUltimateShotOD', 1000)
        if SLOT_ReceivedValue == 404:
            PrivateFunction2('MinervaRecovery', 1000)
        if SLOT_ReceivedValue == 450:
            PrivateFunction2('MinervaAtkBurstDD', 1000)
        if SLOT_ReceivedValue == 500:
            SLOT_6 = 0
            PrivateFunction2('MinervaAtkAstralHeat', 1000)
        if SLOT_ReceivedValue == 600:
            PrivateFunction2('MinervaEntry01', 1000)
        if SLOT_ReceivedValue == 601:
            PrivateFunction2('MinervaEntry01Finish', 1000)
        if SLOT_ReceivedValue == 602:
            PrivateFunction2('MinervaEntry02', 1000)
        if SLOT_ReceivedValue == 607:
            PrivateFunction2('MinervaEntry03', 1000)
        if SLOT_ReceivedValue == 608:
            PrivateFunction2('MinervaEntry03Finish', 1000)
        if SLOT_ReceivedValue == 603:
            PrivateFunction2('MinervaRoundWin', 1000)
        if SLOT_ReceivedValue == 604:
            PrivateFunction2('MinervaWin01', 1000)
        if SLOT_ReceivedValue == 605:
            PrivateFunction2('MinervaWin02', 1000)
        if SLOT_ReceivedValue == 606:
            PrivateFunction2('MinervaLose', 1000)
        if SLOT_ReceivedValue == 650:
            PrivateFunction2('MinervaEventStay', 1000)
        if SLOT_ReceivedValue == 651:
            PrivateFunction2('MinervaEventStayFaceUp', 1000)
        if SLOT_ReceivedValue == 652:
            PrivateFunction2('MinervaEventStayToStand', 1000)
        if SLOT_ReceivedValue == 660:
            PrivateFunction2('MinervaEventWalk', 1000)
        if SLOT_ReceivedValue == 661:
            PrivateFunction2('MinervaEventWalkFast', 1000)
        if SLOT_ReceivedValue == 652:
            PrivateFunction2('MinervaEventReaction2Stand', 1000)
        if SLOT_ReceivedValue == 999:
            if SLOT_51:
                SLOT_51 = 0
                SLOT_52 = 0
                SLOT_53 = 0
            if not SLOT_4:
                if not SLOT_ReceivedValue == 999:
                    PrivateFunction2('MinervaStand', 900)


@Subroutine
def MV_HitBack():
    Unknown9219(1)
    E0EAEffectPosition(3)

    def upon_STATE_END():
        E0EAEffectPosition(0)


@State
def MinervaStand():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        SLOT_6 = 0
        TeleportToObject(3)
        AddX(-100000)
    label(0)
    sprite('mv000_00', 7)
    PrivateFunction3(3, -100000, 0, 20, 0)
    sprite('mv000_01', 7)
    sprite('mv000_02', 7)
    sprite('mv000_03', 7)
    sprite('mv000_04', 7)
    sprite('mv000_05', 7)
    sprite('mv000_06', 7)
    sprite('mv000_07', 7)
    sprite('mv000_08', 7)
    sprite('mv000_09', 7)
    loopRest()
    gotoLabel(0)


@State
def MinervaTurn():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
    sprite('mv000_00ex00', 1)
    PrivateFunction3(3, -100000, 0, 20, 0)
    sprite('mv003_00', 2)
    sprite('mv003_01', 3)
    sprite('mv003_00ex', 3)
    sprite('keep', 100)
    PrivateFunction2('MinervaStand', 100)


@State
def MinervaFWalk():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
    sprite('mv030_00', 7)
    PrivateFunction3(3, -100000, 0, 20, 0)
    label(0)
    sprite('mv030_01', 7)
    CreateParticle('ceef_arukieff00', 0)
    CreateParticle('ceef_arukieff00', 1)
    sprite('mv030_02', 7)
    CreateParticle('ceef_arukieff00', 0)
    CreateParticle('ceef_arukieff00', 1)
    sprite('mv030_03', 7)
    CreateParticle('ceef_arukieff00', 0)
    CreateParticle('ceef_arukieff00', 1)
    sprite('mv030_04', 7)
    CreateParticle('ceef_arukieff00', 0)
    CreateParticle('ceef_arukieff00', 1)
    sprite('mv030_05', 7)
    CreateParticle('ceef_arukieff00', 0)
    CreateParticle('ceef_arukieff00', 1)
    sprite('mv030_06', 7)
    CreateParticle('ceef_arukieff00', 0)
    CreateParticle('ceef_arukieff00', 1)
    loopRest()
    gotoLabel(0)


@State
def MinervaBWalk():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
    sprite('mv031_00', 7)
    PrivateFunction3(3, -100000, 0, 20, 0)
    label(0)
    sprite('mv031_01', 7)
    CreateParticle('ceef_barukieff00', 0)
    CreateParticle('ceef_barukieff00', 1)
    sprite('mv031_02', 7)
    CreateParticle('ceef_barukieff00', 0)
    CreateParticle('ceef_barukieff00', 1)
    sprite('mv031_03', 7)
    CreateParticle('ceef_barukieff00', 0)
    CreateParticle('ceef_barukieff00', 1)
    sprite('mv031_04', 7)
    CreateParticle('ceef_barukieff00', 0)
    CreateParticle('ceef_barukieff00', 1)
    sprite('mv031_05', 7)
    CreateParticle('ceef_barukieff00', 0)
    CreateParticle('ceef_barukieff00', 1)
    sprite('mv031_06', 7)
    loopRest()
    gotoLabel(0)


@State
def MinervaHold():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        SLOT_51 = 1
    label(0)
    sprite('mv000_00', 7)
    sprite('mv000_01', 7)
    sprite('mv000_02', 7)
    sprite('mv000_03', 7)
    sprite('mv000_04', 7)
    sprite('mv000_05', 7)
    sprite('mv000_06', 7)
    sprite('mv000_07', 7)
    sprite('mv000_08', 7)
    sprite('mv000_09', 7)
    loopRest()
    gotoLabel(0)


@State
def MinervaSlowHoming():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        SLOT_51 = 1
        SLOT_52 = 1
    sprite('mv030_00', 2)
    label(0)
    sprite('mv030_01', 7)
    CreateParticle('ceef_arukieff00', 0)
    CreateParticle('ceef_arukieff00', 1)
    sprite('mv030_02', 7)
    CreateParticle('ceef_arukieff00', 0)
    CreateParticle('ceef_arukieff00', 1)
    sprite('mv030_03', 7)
    CreateParticle('ceef_arukieff00', 0)
    CreateParticle('ceef_arukieff00', 1)
    sprite('mv030_04', 7)
    CreateParticle('ceef_arukieff00', 0)
    CreateParticle('ceef_arukieff00', 1)
    sprite('mv030_05', 7)
    CreateParticle('ceef_arukieff00', 0)
    CreateParticle('ceef_arukieff00', 1)
    sprite('mv030_06', 7)
    loopRest()
    gotoLabel(0)


@State
def dengeki_mv():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        E0EAEffectObjectZ(2)
        SetZVal(100)

        def upon_16():
            SkeletonPaletteEffectOnNoStopIdling()
    label(0)
    sprite('ce082_00m', 2)
    sprite('ce082_01m', 2)
    loopRest()
    gotoLabel(0)


@State
def MinervaAtk5B():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_AtkInit')
        callSubroutine('MV_ChainAtkInit')
        callSubroutine('MV_HitBack')
        AttackLevel_(3)
        Damage(600)
    sprite('mv201_00', 3)
    sprite('mv201_01', 3)
    physicsXImpulse(30000)
    SLOT_51 = 1
    SLOT_52 = 3
    sprite('mv201_02', 3)
    XImpulseAcceleration(50)
    CommonSE('004_swing_grap_1_1')
    SLOT_51 = 1
    SLOT_52 = 0
    sprite('mv201_03', 3)
    XImpulseAcceleration(50)
    RefreshMultihit()
    sprite('mv201_04', 2)
    XImpulseAcceleration(0)
    sprite('mv201_05', 4)
    sprite('mv201_06', 4)
    sprite('mv201_07', 4)
    SLOT_51 = 0
    sprite('mv201_08', 4)
    sprite('keep', 100)
    PrivateFunction2('MinervaStand', 100)


@State
def MinervaAtk5C():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_AtkInit')
        callSubroutine('MV_ChainAtkInit')
        callSubroutine('MV_HitBack')
        AttackLevel_(4)
        Damage(900)
        AirPushbackY(15000)
        SingleProration(1)
        Hitstun(19)
        UseSlashHitspark(1)
        HitsparkSize(700)
        PushbackX(17000)
    sprite('mv202_00', 2)
    sprite('mv202_01', 3)
    sprite('mv202_02', 3)
    sprite('mv202_03', 2)
    physicsXImpulse(0)
    sprite('mv202_04', 2)
    XImpulseAcceleration(150)
    CommonSE('010_swing_sword_1')
    CommonSE('004_swing_grap_1_1')
    PrivateSE('cese_06')
    sprite('mv202_05', 2)
    RefreshMultihit()
    AirPushbackY(15000)
    XImpulseAcceleration(25)
    CreateObject('mv202Eff', 100)
    sprite('mv202_06', 2)
    XImpulseAcceleration(0)
    sprite('mv202_07', 2)
    sprite('mv202_08', 2)
    DespawnEAEffect('mv202Eff')
    sprite('mv202_09', 2)
    sprite('mv202_10', 2)
    sprite('mv202_11', 2)
    sprite('mv202_12', 2)
    sprite('mv202_13', 4)
    SLOT_51 = 0
    sprite('mv202_14', 3)
    sprite('keep', 100)
    PrivateFunction2('MinervaStand', 100)


@State
def MinervaAtk2B():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_AtkInit')
        callSubroutine('MV_ChainAtkInit')
        callSubroutine('MV_HitBack')
        AttackLevel_(2)
        Damage(350)
        AttackP1(90)
        SingleProration(1)
        PushbackX(5000)
        UseSlashHitspark(1)
        HitLow(2)
        MoveAttributes(0, 0, 1, 0, 0)
    sprite('mv231_00', 2)
    sprite('mv231_01', 3)
    sprite('mv231_02', 3)
    sprite('mv231_03', 3)
    physicsXImpulse(25000)
    RefreshMultihit()
    CommonSE('010_swing_sword_0')
    CommonSE('004_swing_grap_1_0')
    PrivateSE('cese_05')
    sprite('mv231_04', 3)
    RefreshMultihit()
    XImpulseAcceleration(25)
    sprite('mv231_05', 3)
    XImpulseAcceleration(0)
    sprite('mv231_06', 3)
    sprite('mv231_07', 3)
    SLOT_51 = 0
    sprite('mv231_08', 3)
    sprite('keep', 100)
    PrivateFunction2('MinervaStand', 100)


@State
def MinervaAtk2C():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_AtkInit')
        callSubroutine('MV_ChainAtkInit')
        callSubroutine('MV_HitBack')
        AttackLevel_(4)
        Damage(850)
        AirPushbackY(20000)
        AirPushbackX(-10000)
        PushbackX(-8000)
        UseSlashHitspark(1)
        FatalCounter(1)
        MoveAttributes(0, 1, 0, 0, 0)
    sprite('mv232_00', 3)
    sprite('mv232_01', 4)
    sprite('mv232_02', 4)
    sprite('mv232_03', 2)
    CommonSE('010_swing_sword_1')
    CommonSE('004_swing_grap_1_1')
    PrivateSE('cese_06')
    sprite('mv232_04', 3)
    RefreshMultihit()
    CreateObject('mv232Eff', -1)
    sprite('mv232_05', 2)
    sprite('mv232_06', 2)
    sprite('mv232_07', 2)
    sprite('mv232_08', 3)
    sprite('mv232_09', 3)
    SLOT_51 = 0
    sprite('mv232_10', 3)
    sprite('keep', 100)
    PrivateFunction2('MinervaStand', 100)


@State
def MinervaAtk3C():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_AtkInit')
        callSubroutine('MV_ChainAtkInit')
        callSubroutine('MV_HitBack')
        AttackLevel_(3)
        Damage(750)
        AttackP2(79)
        UseSlashHitspark(1)
        HitLow(2)
        MoveAttributes(0, 0, 1, 0, 0)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(2000)
        AirPushbackY(16000)
        AirUntechableTime(40)
        CHHardKnockdown(1)
    sprite('mv236_00', 3)
    sprite('mv236_01', 3)
    sprite('mv236_02', 3)
    sprite('mv236_03', 3)
    CommonSE('010_swing_sword_1')
    CommonSE('004_swing_grap_1_1')
    PrivateSE('cese_06')
    sprite('mv236_04', 3)
    RefreshMultihit()
    CreateObject('mv236Eff', -1)
    sprite('mv236_05', 3)
    sprite('mv236_06', 3)
    sprite('mv236_07', 3)
    sprite('mv236_08', 3)
    sprite('mv236_09', 3)
    SLOT_51 = 0
    sprite('mv236_10', 3)
    sprite('keep', 100)
    PrivateFunction2('MinervaStand', 100)


@State
def MinervaAtk6B():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_AtkInit')
        callSubroutine('MV_ChainAtkInit')
        callSubroutine('MV_HitBack')
        AttackLevel_(3)
        Damage(700)
        AttackP1(80)
        AirPushbackY(-50000)
        GroundBounce(1)
        BouncePercentage(50)
        UseSlashHitspark(1)
        AirUntechableTime(23)
        CHAirPushbackX(5000)
        CHAirPushbackY(-60000)
        CHAirUntechableTime(45)
        CHBouncePercentage(45)
        CHAirHitstunAnimation(9)
        CHGroundedHitstunAnimation(9)
    sprite('mv211_00', 2)
    sprite('mv211_01', 3)
    sprite('mv211_02', 2)
    sprite('mv211_03', 2)
    sprite('mv211_04', 2)
    CommonSE('004_swing_grap_1_1')
    PrivateSE('cese_05')
    physicsXImpulse(20000)
    sprite('mv211_05', 3)
    XImpulseAcceleration(50)
    RefreshMultihit()
    CreateObject('mv211Eff', -1)
    sprite('mv211_06', 3)
    XImpulseAcceleration(50)
    sprite('mv211_07', 3)
    XImpulseAcceleration(0)
    sprite('mv211_08', 3)
    sprite('mv211_09', 3)
    sprite('mv211_10', 3)
    SLOT_51 = 0
    sprite('mv211_11', 3)
    sprite('keep', 100)
    PrivateFunction2('MinervaStand', 100)


@State
def MinervaAtk6C():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_AtkInit')
        callSubroutine('MV_ChainAtkInit')
        callSubroutine('MV_HitBack')
        AttackLevel_(5)
        Damage(1000)
        AttackP1(90)
        AttackP2(82)
        BonusProration(110)
        GroundedHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(-4500)
        AirPushbackY(37000)
        PushbackX(-16000)
        UseSlashHitspark(1)
        AirUntechableTime(40)
    sprite('mv212_00', 2)
    sprite('mv212_01', 3)
    sprite('mv212_02', 3)
    sprite('mv212_03', 5)
    sprite('mv212_04', 3)
    sprite('mv212_05', 2)
    sprite('mv212_06', 2)
    CommonSE('010_swing_sword_2')
    CommonSE('004_swing_grap_1_2')
    PrivateSE('cese_06')
    sprite('mv212_07', 3)
    RefreshMultihit()
    CreateObject('mv212Eff', -1)
    sprite('mv212_08', 2)
    SLOT_51 = 0
    sprite('mv212_09', 2)
    sprite('mv212_10', 2)
    sprite('mv212_11', 4)
    sprite('mv212_12', 5)
    sprite('mv212_13', 3)
    sprite('mv212_14', 3)
    sprite('keep', 100)
    PrivateFunction2('MinervaStand', 100)


@State
def MinervaAtkAIR5B():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_AtkInit')
        SLOT_51 = 1
        SLOT_52 = 4
        SLOT_53 = 1
        Unknown9219(1)
        AttackLevel_(2)
        Damage(650)
        AttackP1(80)
        UseSlashHitspark(1)
        HitAirUnblockable(0)
        HitOverhead(2)
        MoveAttributes(1, 0, 0, 0, 0)
    sprite('mv251_00', 2)
    TeleportToObject(3)
    sprite('mv251_01', 3)
    sprite('mv251_02', 3)
    sprite('mv251_03', 3)
    RefreshMultihit()
    CreateObject('mv251Eff', -1)

    def RunOnObject_1():
        AddY(40000)
    CommonSE('004_swing_grap_1_0')
    PrivateSE('cese_05')
    sprite('mv251_04', 3)
    SetZVal(500)
    sprite('mv251_05', 3)
    sprite('mv251_06', 3)
    sprite('mv251_07', 3)
    sprite('mv251_08', 32767)
    sprite('keep', 100)
    PrivateFunction2('MinervaStand', 100)


@State
def MinervaAtkAIR5C():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_AtkInit')
        SLOT_51 = 1
        SLOT_52 = 4
        SLOT_53 = 1
        Unknown9219(1)
        AttackLevel_(3)
        Damage(550)
        AttackP1(80)
        SingleProration(1)
        AirUntechableTime(20)
        Hitstop(9)
        AirPushbackY(22000)
        UseSlashHitspark(1)
        HitAirUnblockable(0)
        HitOverhead(2)
        MoveAttributes(1, 0, 0, 0, 0)
    sprite('mv252_00', 2)
    TeleportToObject(3)
    sprite('mv252_01', 3)
    sprite('mv252_02', 3)
    sprite('mv252_03', 3)
    CommonSE('004_swing_grap_1_1')
    PrivateSE('cese_06')
    sprite('mv252_04', 2)
    RefreshMultihit()
    CreateObject('mv252Eff', -1)
    sprite('mv252_04', 2)
    StartMultihit()
    sprite('mv252_05', 2)
    RefreshMultihit()
    sprite('mv252_04', 2)
    StartMultihit()
    sprite('mv252_06', 3)
    SetZVal(500)
    sprite('mv252_07', 3)
    sprite('mv252_08', 3)
    sprite('mv252_09', 3)
    sprite('mv252_10', 32767)
    sprite('keep', 100)
    PrivateFunction2('MinervaStand', 100)


@State
def MinervaAtkShot():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_ChainAtkInit')
        callSubroutine('MV_HitBack')
    sprite('mv403_00', 2)
    sprite('mv403_02', 2)
    CreateObject('mv403ConsentEff', 0)
    sprite('mv403_03', 1)
    sprite('mv403_04', 1)
    sprite('mv403_05', 2)
    AltKnockdownEffects(100, 1, 1)
    PrivateSE('cese_15')
    sprite('mv403_06', 2)
    sprite('mv403_07', 2)
    sprite('mv403_08', 3)
    CreateObject('ShotAtkObj', 0)
    sprite('mv403_09', 3)
    sprite('mv403_10', 3)
    sprite('mv403_11', 3)
    sprite('mv403_12', 3)
    TriggerUponForState('mv403ConsentEff', 32)
    sprite('mv403_13', 3)
    SLOT_51 = 0
    sprite('mv403_15', 3)
    sprite('keep', 100)
    PrivateFunction2('MinervaStand', 100)


@State
def ShotAtkObj():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        CollideWithWall(1)
        PaletteIndex(1)
        AttackLevel_(3)
        Damage(900)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(90)
        Hitstop(0)
        EnemyHitstopAddition(6, 6, 8)
        AttackDirection(2)
        AirUntechableTime(33)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackY(24000)
        SetZVal(-500)
        Unknown12052(1)
        AddY(-70000)
        Size(800)
        SLOT_5 = 1

        def upon_STATE_END():
            SLOT_5 = 0
        RunLoopUpon(17, 50)

        def upon_17():
            sendToLabel(1)
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 0)
        uponSendToLabel(54, 2)
        AttackOff()
    sprite('vrceef999_99test', 5)
    SetScaleSpeed(40)
    physicsXImpulse(100)
    CreateObject('mv403Nokosistart', 100)
    CreateObject('mv403ShotEff', 100)
    Visibility(1)
    sprite('vrceef999_99test', 10)
    Size(1000)
    SetScaleSpeed(0)
    RefreshMultihit()
    physicsXImpulse(43000)
    SetAcceleration(-1000)
    label(0)
    sprite('vrceef999_99test', 6)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrceef999_99test2', 3)
    TriggerUponForState('mv403ShotEff', 32)
    clearUponHandler(17)
    physicsXImpulse(0)
    SetAcceleration(0)
    ExitState()
    label(2)
    sprite('null', 10)
    TriggerUponForState('mv403ShotEff', 32)
    clearUponHandler(17)
    clearUponHandler(54)
    physicsXImpulse(0)
    SetAcceleration(0)


@State
def MinervaAtkAirAssault():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        IgnorePauses(3)
        SLOT_53 = 1
        FloorCollision(1)

        def upon_EVERY_FRAME():
            if not SLOT_51:
                if SLOT_IsAirborne:
                    PrivateFunction3(3, 0, 0, 25, 0)
                else:
                    PrivateFunction3(3, -100000, 0, 25, 0)
            if SLOT_54 == 1:
                PrivateFunction3(3, -100000, 200000, 100, 0)
            if SLOT_54 == 2:
                PrivateFunction3(3, 0, -10000, 50, 0)
                physicsYImpulse(-20000)
            if SLOT_54 == 3:
                PrivateFunction3(3, 0, 0, 100, 0)
            if SLOT_55:
                TeleportToObject(3)
                AddX(-100000)

        def upon_32():
            SLOT_54 = 2
            sendToLabel(1)
        uponSendToLabel(LANDING, 2)
    sprite('mv404_00', 3)
    TeleportToObject(3)
    SLOT_54 = 3
    SLOT_51 = 1
    sprite('mv404_01', 3)
    sprite('mv404_02', 3)
    sprite('mv404_03', 3)
    sprite('mv404_04', 3)
    sprite('mv404_05', 3)
    sprite('mv404_06', 3)
    sprite('mv404_07', 3)
    SLOT_54 = 1
    SLOT_51 = 1
    label(0)
    sprite('mv404_08', 3)
    sprite('mv404_07', 3)
    gotoLabel(0)
    label(1)
    sprite('mv404_07', 3)
    sprite('mv404_08', 3)
    gotoLabel(1)
    label(2)
    sprite('mv212_11', 3)
    clearUponHandler(LANDING)
    EndMomentum(1)
    SLOT_55 = 1
    AltKnockdownEffects(100, 1, 1)
    sprite('mv212_12', 3)
    sprite('mv212_13', 3)
    sprite('mv212_14', 3)
    sprite('keep', 100)
    PrivateFunction2('MinervaStand', 100)


@State
def MinervaAtkUltimateShot():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        AttackDefaults_SuperProjectile()
        callSubroutine('MV_ChainAtkInit')
        AttackLevel_(3)
        UseSlashHitspark(1)
        Damage(150)
        MinimumDamage(15)
        AttackP1(100)
        AttackP2(69)
        SingleProration(1)
        AirPushbackX(35000)
        AirPushbackY(25000)
        AirHitstunAnimation(19)
        GroundedHitstunAnimation(19)
        AirUntechableTime(60)
        Hitstop(0)
        EnemyHitstopAddition(0, 2, 7)
        StarterRating(2)
        SLOT_54 = 10

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            if SLOT_54 == 1:
                Damage(1000)
                MinimumDamage(20)
                PushbackX(20000)
                AirHitstunAnimation(13)
                GroundedHitstunAnimation(13)
    sprite('mv000_00', 3)
    sprite('mv403_00', 3)
    sprite('mv403_01', 3)
    sprite('mv403_02', 3)
    CreateObject('mv403ConsentEff', 0)
    CreateObject('mv403TameEff', -1)
    CreateObject('mv403TameEffSub', -1)
    sprite('mv403_03', 3)
    sprite('mv403_17', 3)
    AltKnockdownEffects(100, 1, 1)
    PrivateSE('cese_15')
    sprite('mv403_18', 6)
    sprite('mv403_19', 46)
    CreateObject('mv403Eff', 100)
    sprite('mv403_20', 2)
    RefreshMultihit()
    DespawnEAEffect('mv403TameEffSub')
    TriggerUponForState('mv403Eff', 32)
    TriggerUponForState('mv403TameEff', 32)
    sprite('mv403_21', 1)
    StartMultihit()
    sprite('mv403_21', 1)
    RefreshMultihit()
    sprite('mv403_22', 1)
    sprite('mv403_22', 1)
    StartMultihit()
    SLOT_54 = SLOT_54 + -1
    if SLOT_54 > 0:
        sendToLabel(0)
    label(0)
    sprite('mv403_20', 2)
    RefreshMultihit()
    sprite('mv403_21', 1)
    StartMultihit()
    sprite('mv403_21', 1)
    RefreshMultihit()
    sprite('mv403_22', 1)
    sprite('mv403_22', 1)
    StartMultihit()
    SLOT_54 = SLOT_54 + -1
    if SLOT_54 > 0:
        sendToLabel(0)
    label(1)
    sprite('mv403_23', 10)
    DespawnEAEffect('mv403Eff')
    CreateParticle('ceef_403beamend00', 0)
    CreateParticle('ceef_403beamend00', 1)
    CreateParticle('ceef_403beamend00', 2)
    sprite('mv403_24', 5)
    sprite('mv403_25', 5)
    sprite('mv403_14', 5)
    TriggerUponForState('mv403ConsentEff', 32)
    sprite('mv403_15', 5)
    sprite('mv403_16', 5)
    sprite('keep', 100)
    PrivateFunction2('MinervaStand', 100)


@State
def MinervaAtkUltimateShotOD():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        AttackDefaults_SuperProjectile()
        AttackLevel_(3)
        AttackType(4)
        UseSlashHitspark(1)
        Damage(200)
        MinimumDamage(15)
        AttackP1(100)
        AttackP2(69)
        SingleProration(1)
        AirPushbackX(35000)
        AirPushbackY(25000)
        AirHitstunAnimation(19)
        GroundedHitstunAnimation(19)
        AirUntechableTime(60)
        Hitstop(0)
        EnemyHitstopAddition(0, 2, 7)
        StarterRating(2)
        SLOT_54 = 10

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            if SLOT_54 == 1:
                Damage(1250)
                MinimumDamage(20)
                PushbackX(20000)
                AirHitstunAnimation(13)
                GroundedHitstunAnimation(13)
    sprite('mv000_00', 3)
    sprite('mv403_00', 3)
    TeleportToObject(3)
    AddX(-100000)
    sprite('mv403_01', 3)
    sprite('mv403_02', 3)
    CreateObject('mv403TameEffOD', -1)
    CreateObject('mv403ConsentEff', 0)
    CreateObject('mv403TameEffSub', -1)
    sprite('mv403_03', 3)
    sprite('mv403_17', 3)
    AltKnockdownEffects(100, 1, 1)
    PrivateSE('cese_15')
    sprite('mv403_18', 6)
    sprite('mv403_19', 46)
    CreateObject('mv403EffOD', 100)
    sprite('mv403_20', 2)
    RefreshMultihit()
    DespawnEAEffect('mv403TameEffSub')
    TriggerUponForState('mv403EffOD', 32)
    TriggerUponForState('mv403TameEffOD', 32)
    sprite('mv403_21', 1)
    StartMultihit()
    sprite('mv403_21', 1)
    RefreshMultihit()
    sprite('mv403_22', 1)
    sprite('mv403_22', 1)
    StartMultihit()
    SLOT_54 = SLOT_54 + -1
    if SLOT_54 > 0:
        sendToLabel(0)
    label(0)
    sprite('mv403_20', 2)
    RefreshMultihit()
    sprite('mv403_21', 1)
    StartMultihit()
    sprite('mv403_21', 1)
    RefreshMultihit()
    sprite('mv403_22', 1)
    sprite('mv403_22', 1)
    StartMultihit()
    SLOT_54 = SLOT_54 + -1
    if SLOT_54 > 0:
        sendToLabel(0)
    label(1)
    sprite('mv403_23', 10)
    TriggerUponForState('mv403EffOD', 33)
    CreateParticle('ceef_403beamend00', 0)
    CreateParticle('ceef_403beamend00', 1)
    CreateParticle('ceef_403beamend00', 2)
    sprite('mv403_24', 5)
    sprite('mv403_25', 5)
    sprite('mv403_14', 5)
    TriggerUponForState('mv403ConsentEff', 32)
    sprite('mv403_15', 5)
    sprite('mv403_16', 5)
    sprite('keep', 100)
    PrivateFunction2('MinervaStand', 100)


@State
def MinervaRecovery():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        uponSendToLabel(32, 0)
    sprite('mv601_03', 6)
    sprite('mv615_00', 6)
    sprite('mv615_01', 6)
    sprite('mv601_00', 32767)
    label(0)
    sprite('mv615_01', 6)
    sprite('mv615_00', 6)
    sprite('mv601_03', 6)
    sprite('keep', 100)
    PrivateFunction2('MinervaStand', 100)


@State
def MinervaAtkBurstDD():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(460)
        Hitstop(8)
        HeatGainMultiplier(0)
        ChipPercentage(0)
        MinimumDamage(10)
        AirUntechableTime(100)
        AttackP2(100)
        SingleProration(1)
        PushbackX(20000)
        UseSlashHitspark(1)
        DefeatOpponentBehavior(1)
        DamageFromStateOnly('MinervaAtkBurstDD')
        OnlyHitPlayer(1)
        HitAnywhere(1)
        CopyFromRightToLeft(23, 2, 55, 3, 2, 51)
    sprite('mv236_00ex01', 3)
    SLOT_51 = 4
    sprite('mv236_01ex01', 3)
    sprite('mv236_02ex01', 3)
    sprite('mv236_03ex01', 3)
    CommonSE('010_swing_sword_1')
    CommonSE('004_swing_grap_1_1')
    PrivateSE('cese_06')
    sprite('mv236_04ex01', 3)
    CreateObject('ce440Eff', -1)
    CreateObject('mv236Eff', -1)
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    RefreshMultihit()
    sprite('mv236_05ex01', 3)
    sprite('mv236_06ex01', 3)
    TriggerUponForState('BurstDDAdd', 33)
    sprite('mv232_02ex01', 3)
    physicsXImpulse(30000)
    SetAcceleration(-3000)
    sprite('mv232_03ex01', 3)
    CommonSE('010_swing_sword_1')
    CommonSE('004_swing_grap_1_1')
    PrivateSE('cese_06')
    sprite('mv232_04ex01', 3)
    CreateObject('ce440Eff2', -1)
    CreateObject('mv232Eff', -1)
    AirHitstunAnimation(4)
    GroundedHitstunAnimation(4)
    PushbackX(-5000)
    RefreshMultihit()
    EndMomentum(1)
    sprite('mv232_05ex01', 3)
    sprite('mv232_06ex01', 3)
    TriggerUponForState('BurstDDAdd', 34)
    sprite('mv212_05ex01', 3)
    physicsYImpulse(18000)
    setGravity(2000)

    def upon_LANDING():
        clearUponHandler(LANDING)
        EndMomentum(1)
    sprite('mv212_06ex01', 3)
    CommonSE('010_swing_sword_2')
    CommonSE('004_swing_grap_1_2')
    PrivateSE('cese_06')
    physicsXImpulse(-18000)
    sprite('mv212_07ex01', 3)
    CreateObject('ce440Eff3', -1)
    CreateObject('mv212Eff', -1)
    AirHitstunAnimation(17)
    GroundedHitstunAnimation(17)
    AirPushbackX(-1000)
    AirPushbackY(28000)
    RefreshMultihit()
    sprite('mv212_08ex01', 3)
    CreateObject('ce440Eff3', -1)
    sprite('mv212_09ex01', 3)
    sprite('mv212_10ex01', 3)
    sprite('mv212_11ex01', 3)
    loopRest()
    if SLOT_55:
        conditionalSendToLabel(100)
    sprite('mv403_00ex01', 3)
    sprite('mv403_01ex01', 3)
    TriggerUponForState('BurstDDAdd', 35)
    sprite('mv403_02ex01', 3)
    sprite('mv440_00', 3)
    CreateObject('ce440EffMato', -1)
    physicsXImpulse(3000)
    sprite('mv440_01', 3)
    physicsXImpulse(30000)
    PrivateSE('cese_10')
    sprite('mv440_02', 1)
    CreateObject('mv403ConsentEff', 0)

    def RunOnObject_1():
        Rotation(90000)
    CreateObject('mv440Eff', -1)
    Damage(1000)
    EnemyHitstopAddition(-1, -1, -1)
    AirHitstunAnimation(19)
    GroundedHitstunAnimation(19)
    AirPushbackX(50000)
    AirPushbackY(18000)
    UseSlashHitspark(0)
    Hitstop(10)
    DamageEffect(2, 'ceef_hiteff440')
    Floorslide(15)
    AttackType(4)
    DefeatOpponentBehavior(0)
    RefreshMultihit()
    EndMomentum(1)
    TriggerUponForState('BurstDDAdd', 41)
    sprite('mv440_03', 3)
    DespawnEAEffect('BurstDD_Camera')
    ScreenShake(40000, 40000)
    DespawnEAEffect('ce440EffMato')
    TriggerUponForState('mv440Eff', 32)
    sprite('mv440_04', 3)
    sprite('mv440_05', 3)
    sprite('mv202_09ex01', 4)
    sprite('mv202_10ex01', 5)
    TriggerUponForState('mv403ConsentEff', 32)
    sprite('mv202_11ex01', 5)
    sprite('mv202_12ex01', 5)
    sprite('mv202_13ex01', 5)
    SLOT_51 = 0
    sprite('mv202_14ex01', 5)
    sprite('keep', 100)
    PrivateFunction2('MinervaStand', 100)
    label(100)
    sprite('mv403_00ex01', 3)
    sprite('mv403_01ex01', 3)
    sprite('mv403_02ex01', 3)
    TriggerUponForState('BurstDDAdd', 35)
    sprite('mv440_00', 3)
    CreateObject('ce440EffMato', -1)
    physicsXImpulse(3000)
    sprite('mv440_01', 3)
    physicsXImpulse(30000)
    PrivateSE('cese_10')
    sprite('mv440_02', 3)
    CreateObject('mv403ConsentEff', 0)
    CreateObject('mv440Eff', -1)
    Damage(630)
    Hitstop(0)
    EnemyHitstopAddition(1, 1, 1)
    AirHitstunAnimation(19)
    GroundedHitstunAnimation(19)
    AirPushbackX(20000)
    AirPushbackY(2500)
    Floorslide(15)
    HitsparkSize(700)
    RefreshMultihit()
    EndMomentum(1)
    UseSlashHitspark(0)
    Hitstop(3)
    DamageEffect(2, 'ceef_hiteff440')
    sprite('mv440_02ex01', 3)
    RefreshMultihit()
    PrivateSE('cese_10')
    sprite('mv440_02ex02', 3)
    RefreshMultihit()
    PrivateSE('cese_10')
    sprite('mv440_02', 3)
    RefreshMultihit()
    PrivateSE('cese_10')
    sprite('mv440_02ex01', 3)
    RefreshMultihit()
    PrivateSE('cese_10')
    sprite('mv440_02ex02', 3)
    AirPushbackX(50000)
    AirPushbackY(18000)
    AttackType(4)
    DefeatOpponentBehavior(0)
    RefreshMultihit()
    TriggerUponForState('BurstDDAdd', 41)
    sprite('mv440_03', 3)
    DespawnEAEffect('BurstDD_Camera')
    DespawnEAEffect('ce440EffMato')
    TriggerUponForState('mv440Eff', 32)
    sprite('mv440_04', 3)
    CreateObject('ceef_hiteff440HitEx', -1)
    sprite('mv440_05', 3)
    sprite('mv202_09ex01', 4)
    sprite('mv202_10ex01', 5)
    TriggerUponForState('mv403ConsentEff', 32)
    sprite('mv202_11ex01', 5)
    sprite('mv202_12ex01', 5)
    sprite('mv202_13ex01', 5)
    SLOT_51 = 0
    sprite('mv202_14ex01', 5)
    sprite('keep', 100)
    PrivateFunction2('MinervaStand', 100)


@State
def ThrowUpCelica():

    def upon_IMMEDIATE():
        AddY(100000)
        physicsYImpulse(70000)
        IgnoreScreenfreeze(1)
        NoDamageAction(1)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
    sprite('ce430_00', 3)
    sprite('ce430_01', 3)
    sprite('ce430_00', 3)
    sprite('ce430_01', 3)
    sprite('ce430_00', 3)


@State
def ThrowDownCelica():

    def upon_IMMEDIATE():
        AddY(2000000)
        NoDamageAction(1)
        AlphaValue(0)
        ConstantAlphaModifier(31)

        def upon_EVERY_FRAME():
            PrivateFunction3(3, 35000, 0, 8, 0)
            if SLOT_YDistanceFromFloor <= 250000:
                ObjectUpon(EVERY_FRAME, 32)
                sendToLabel(1)
    label(0)
    sprite('ce430_02', 3)
    sprite('ce430_03', 3)
    gotoLabel(0)
    label(1)
    sprite('null', 3)
    clearUponHandler(EVERY_FRAME)


@State
def UltimateAssaultAddAttackMissVer():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        Visibility(1)
        NoDamageAction(1)
        AttackLevel_(4)
        Damage(300)
        DefeatOpponentBehavior(1)
        GroundedHitstunAnimation(9)
        PassByArmor(1)
        OnlyHitPlayer(1)
        AttackP1(70)
        PushbackX(-1000)
        AirPushbackX(0)
        AirPushbackY(16000)
        UseSlashHitspark(1)
        Hitstop(4)
        StarterRating(2)

        def upon_EVERY_FRAME():
            TeleportToObject(22)
    sprite('mv430_15', 2)
    RefreshMultihit()
    sprite('mv430_15', 2)
    RefreshMultihit()
    sprite('mv430_15', 2)
    RefreshMultihit()
    sprite('mv430_15', 2)
    RefreshMultihit()
    sprite('mv430_15', 2)
    RefreshMultihit()


@State
def UltimateAssaultAddAttack():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        Visibility(1)
        TeleportToObject(22)
        AttackLevel_(4)
        Damage(200)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP2(100)
        SingleProration(1)
        DefeatOpponentBehavior(1)
        PassByArmor(1)
        OnlyHitPlayer(1)
        AirPushbackX(0)
        AirPushbackY(36000)
        HardKnockdown(30)
        AirUntechableTime(60)
        Hitstop(4)
        DamageEffect(5, '')
        CHStateIfCHStart(3)
        DamageFromStateOnly('UltimateAssaultAddAttack')

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_54 = SLOT_54 + 1
            if SLOT_54 >= 13:
                DamageFromStateOnly('UltimateAssault')
                sendToLabel(1)
        SetActionMark(60)
    label(0)
    sprite('mv430_15', 1)
    AddActionMark(-1)
    RefreshMultihit()
    if SLOT_2:
        conditionalSendToLabel(0)
    label(1)
    sprite('mv430_15', 1)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    sprite('null', 3)
    ObjectUpon(EVERY_FRAME, 33)


@State
def UltimateAssaultAddAttackOD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        Visibility(1)
        TeleportToObject(22)
        AttackLevel_(4)
        Damage(100)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP2(100)
        SingleProration(1)
        DefeatOpponentBehavior(1)
        PassByArmor(1)
        OnlyHitPlayer(1)
        AirPushbackX(0)
        AirPushbackY(36000)
        HardKnockdown(30)
        AirUntechableTime(60)
        Hitstop(4)
        DamageEffect(5, '')
        CHStateIfCHStart(3)
        DamageFromStateOnly('UltimateAssaultAddAttackOD')

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_54 = SLOT_54 + 1
            if SLOT_54 >= 5:
                sendToLabel(100)
        SetActionMark(60)
    label(0)
    sprite('mv430_15', 1)
    AddActionMark(-1)
    RefreshMultihit()
    if SLOT_2:
        conditionalSendToLabel(0)
    label(100)
    sprite('mv430_15', 1)
    Hitstop(2)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)

    def upon_OPPONENT_HIT_OR_BLOCK():
        SLOT_54 = SLOT_54 + 1
        if SLOT_54 >= 17:
            DamageFromStateOnly('UltimateAssaultOD')
            sendToLabel(200)
    SetActionMark(60)
    label(101)
    sprite('mv430_15', 1)
    AddActionMark(-1)
    RefreshMultihit()
    if SLOT_2:
        conditionalSendToLabel(101)
    label(200)
    sprite('mv430_15', 1)
    clearUponHandler(OPPONENT_HIT_OR_BLOCK)
    sprite('null', 3)
    ObjectUpon(EVERY_FRAME, 33)


@State
def MinervaAtkAstralHeat():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        IgnorePauses(3)
        SetZVal(500)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
    sprite('mv000_00', 7)
    sprite('mv000_01', 7)
    sprite('mv000_02', 7)
    sprite('mv000_03', 7)
    sprite('mv000_04', 7)
    sprite('mv000_05', 7)
    sprite('mv000_06', 7)
    sprite('mv000_07', 7)
    sprite('mv000_08', 7)
    sprite('mv000_09', 7)
    sprite('mv000_00', 7)
    sprite('mv000_01', 7)
    sprite('mv000_02', 7)
    sprite('mv000_03', 7)
    sprite('mv000_04', 7)
    sprite('mv000_05', 7)
    sprite('mv000_06', 7)
    sprite('mv000_07', 7)
    sprite('mv000_08', 7)
    sprite('mv000_09', 52)
    sprite('mv450_00', 8)
    TeleportToObject(3)
    AddX(-100000)
    SLOT_51 = 1
    SLOT_53 = 1
    sprite('mv450_01', 8)
    sprite('mv450_02', 8)
    sprite('mv450_03', 8)
    sprite('mv450_04', 8)
    sprite('mv450_05', 6)
    physicsYImpulse(100000)
    ScreenShake(40000, 40000)
    CreateObject('mv450Smoke', -1)
    PrivateSE('cese_09')
    CreateParticle('ceef_450_tobishock', -1)
    CreateObject('mv450Smoke', -1)

    def RunOnObject_1():
        Flip()
    sprite('null', 32767)
    TeleportToObject(3)
    EndMomentum(1)
    AbsoluteY(0)
    label(0)
    sprite('mv450_06', 1)
    EnableAfterimage(1)
    clearUponHandler(32)
    AddX(2000000)
    SetZVal(-500)
    CreateObject('ce450JetEff', 0)
    CreateObject('ce450JetEff', 1)
    CreateObject('ce450JetEff', 2)
    CreateObject('ce450JetEff', 3)
    sprite('mv450_06', 8)
    physicsXImpulse(-150000)
    ForceFaceSprite()
    sprite('mv450_06', 21)
    sprite('mv450_06', 1)
    DespawnEAEffect('ce450JetEff')
    sprite('null', 32767)
    TeleportToObject(3)
    EndMomentum(1)
    AbsoluteY(0)
    SetZVal(500)
    label(1)
    sprite('keep', 1)
    EnableAfterimage(0)
    TeleportToObject(3)
    sprite('mv030_00', 60)
    AddX(-850000)
    sprite('mv030_00', 5)
    physicsXImpulse(11000)
    sprite('mv030_01', 5)
    sprite('mv030_02', 5)
    sprite('mv030_03', 5)
    sprite('mv030_04', 5)
    sprite('mv030_05', 5)
    sprite('mv030_06', 5)
    sprite('mv030_01', 5)
    sprite('mv030_02', 5)
    sprite('mv030_03', 5)
    sprite('mv030_04', 5)
    sprite('mv030_05', 5)
    sprite('mv030_06', 5)
    sprite('keep', 100)
    PrivateFunction2('MinervaStand', 100)


@State
def ceef_hiteffAst():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    CreateParticle('ceef_shungokuodeff_end', -1)
    ScreenShake(20000, 20000)
    PrivateSE('cese_23')


@State
def AstCameraObj():

    def upon_IMMEDIATE():
        CameraControlEnable(1)
        CameraNoCeiling(1)
        CameraNoScreenCollision(1)
        CameraControlInfinity(1)
        CameraWinnerControlStop(1)
        WallCollisionDetection(0)
        ScreenCollision(0)
        TeleportToObject(22)
        uponSendToLabel(32, 1)
    sprite('null', 1)
    sprite('null', 32767)
    AddX(-10000)
    label(1)
    sprite('null', 1)


@State
def AstDeathAttack():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        AttackLevel_(5)
        Damage(20000)
        MinimumDamage(100)
        HitAnywhere(1)
        DefeatOpponentBehavior(3)
        AirPushbackX(-50000)
        AirPushbackY(100000)
        UseFireHitspark(1)
        Visibility(1)
        WallCollisionDetection(0)
        ScreenCollision(0)
        TeleportToObject(22)
    sprite('mv450_06', 10)


@State
def MinervaEntry01():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
    label(1)
    sprite('mv601_00', 3)
    gotoLabel(1)


@State
def MinervaEntry01Finish():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
    sprite('mv601_00', 3)
    sprite('mv601_01', 6)
    sprite('mv601_02', 16)
    sprite('mv601_02ex01', 6)
    sprite('mv601_02ex02', 6)
    sprite('mv601_02ex03', 6)
    sprite('mv601_02ex01', 6)
    sprite('mv601_02ex02', 6)
    sprite('mv601_02ex03', 6)
    sprite('mv601_02ex01', 6)
    sprite('mv601_02ex02', 6)
    sprite('mv601_02ex03', 6)
    sprite('mv601_03', 8)
    sprite('keep', 100)
    PrivateFunction2('MinervaStand', 100)


@State
def MinervaEntry02():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        SLOT_51 = 1
        uponSendToLabel(32, 100)
        uponSendToLabel(33, 200)
        uponSendToLabel(34, 300)
    sprite('mv602_00', 7)
    TeleportToObject(3)
    EndMomentum(1)
    AbsoluteY(0)
    label(0)
    sprite('keep', 1)
    gotoLabel(0)
    label(100)
    sprite('mv602_00', 7)
    label(101)
    sprite('mv602_00', 7)
    gotoLabel(101)
    label(200)
    sprite('keep', 1)
    TeleportToObject(3)
    EndMomentum(1)
    AbsoluteY(0)
    physicsXImpulse(11000)
    sprite('mv602_00', 7)
    sprite('mv602_01', 7)
    sprite('mv602_02', 7)
    sprite('mv602_03', 7)
    sprite('mv602_04', 7)
    sprite('mv602_05', 7)
    label(5)
    sprite('mv602_00', 7)
    sprite('mv602_01', 7)
    sprite('mv602_02', 7)
    sprite('mv602_03', 7)
    sprite('mv602_04', 7)
    sprite('mv602_05', 7)
    gotoLabel(5)
    label(300)
    sprite('mv602_05ex', 5)
    physicsXImpulse(5000)
    sprite('mv602_06', 5)
    physicsXImpulse(0)
    sprite('keep', 100)
    PrivateFunction2('MinervaStand', 100)


@State
def MinervaEntry03():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        clearUponHandler(EVERY_FRAME)
    label(0)
    sprite('mv610_03ex01', 8)
    sprite('mv610_03ex02', 8)
    sprite('mv610_03ex03', 8)
    sprite('mv610_03ex04', 8)
    sprite('mv610_03ex05', 8)
    sprite('mv610_03ex06', 8)
    loopRest()
    gotoLabel(0)


@State
def MinervaEntry03Finish():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        clearUponHandler(EVERY_FRAME)
    sprite('mv610_02', 5)
    sprite('mv610_00', 6)
    sprite('keep', 100)
    PrivateFunction2('MinervaStand', 100)


@State
def MinervaRoundWin():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')

    def upon_32():
        sendToLabel(10)
    sprite('mv030_00', 7)
    PrivateFunction3(3, -100000, 0, 20, 0)
    label(0)
    sprite('mv030_01', 7)
    sprite('mv030_02', 7)
    sprite('mv030_03', 7)
    sprite('mv030_04', 7)
    sprite('mv030_05', 7)
    sprite('mv030_06', 7)
    loopRest()
    gotoLabel(0)
    label(10)
    sprite('mv601_03', 8)
    sprite('mv615_00', 30)
    sprite('mv615_01', 5)
    sprite('mv601_00', 32767)


@State
def MinervaWin01():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
    sprite('mv610_00', 8)
    sprite('mv610_01', 8)
    sprite('mv610_02', 8)
    sprite('mv610_03', 8)
    label(0)
    sprite('mv610_03ex01', 8)
    sprite('mv610_03ex02', 8)
    sprite('mv610_03ex03', 8)
    sprite('mv610_03ex04', 8)
    sprite('mv610_03ex05', 8)
    sprite('mv610_03ex06', 8)
    gotoLabel(0)


@State
def MinervaWin02():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')

    def upon_32():
        sendToLabel(10)

    def upon_41():
        sendToLabel(90)
    sprite('mv030_00', 7)
    PrivateFunction3(3, -100000, 0, 20, 0)
    label(0)
    sprite('mv030_01', 7)
    sprite('mv030_02', 7)
    sprite('mv030_03', 7)
    sprite('mv030_04', 7)
    sprite('mv030_05', 7)
    sprite('mv030_06', 7)
    loopRest()
    gotoLabel(0)
    label(10)
    sprite('mv611_00', 8)
    sprite('mv611_01', 8)
    sprite('mv611_02', 8)
    sprite('mv611_03', 8)
    sprite('mv611_04', 32767)
    label(90)
    sprite('null', 32767)


@State
def MinervaLose():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
    sprite('mv620_00', 6)
    sprite('mv620_01', 6)
    sprite('mv620_01ex1', 6)
    sprite('mv620_01ex2', 6)
    sprite('mv620_01ex3', 6)
    sprite('mv620_01ex4', 6)
    sprite('mv620_01ex5', 6)
    sprite('mv620_01ex6', 6)
    sprite('mv620_01ex1', 6)
    sprite('mv620_01ex2', 6)
    sprite('mv620_01ex3', 6)
    sprite('mv620_01ex4', 6)
    sprite('mv620_01ex5', 6)
    sprite('mv620_01ex6', 6)
    sprite('mv620_02', 6)
    sprite('mv620_03', 32767)


@State
def MinervaStandReaction():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        SLOT_51 = 1
        SLOT_52 = 3
    sprite('mv001_00', 6)
    sprite('mv001_00ex00', 6)
    sprite('mv001_00ex01', 6)
    sprite('mv001_00ex02', 6)
    sprite('mv001_01', 6)
    sprite('mv001_02', 6)
    label(10)
    sprite('mv001_02ex00', 6)
    sprite('mv001_02ex01', 6)
    sprite('mv001_02ex02', 6)
    sprite('mv001_02ex03', 6)
    sprite('mv001_02ex04', 6)
    sprite('mv001_02ex05', 6)
    sprite('mv001_02ex06', 6)
    gotoLabel(10)


@State
def MinervaEventStay():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        clearUponHandler(EVERY_FRAME)
    sprite('mv601_00', 32767)


@State
def MinervaEventStayFaceUp():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        clearUponHandler(EVERY_FRAME)
    sprite('mv601_01', 6)
    sprite('mv601_02', 32767)


@State
def MinervaEventStayToStand():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        clearUponHandler(EVERY_FRAME)
    sprite('mv601_01', 6)
    sprite('mv601_02', 6)
    sprite('mv601_03', 32767)


@State
def MinervaEventWalk():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        clearUponHandler(EVERY_FRAME)
    sprite('mv030_00', 7)
    physicsXImpulse(2000)
    label(0)
    sprite('mv030_01', 7)
    sprite('mv030_02', 7)
    sprite('mv030_03', 7)
    sprite('mv030_04', 7)
    sprite('mv030_05', 7)
    sprite('mv030_06', 7)
    loopRest()
    gotoLabel(0)


@State
def MinervaEventWalkFast():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
    sprite('mv030_00', 7)
    label(0)
    sprite('mv030_01', 7)
    sprite('mv030_02', 7)
    sprite('mv030_03', 7)
    sprite('mv030_04', 7)
    sprite('mv030_05', 7)
    sprite('mv030_06', 7)
    loopRest()
    gotoLabel(0)


@State
def MinervaEventReaction2Stand():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        SLOT_51 = 1
        SLOT_52 = 3
    sprite('mv001_02', 6)
    sprite('mv001_01', 6)
    sprite('mv001_00ex00', 6)
    sprite('mv001_00', 32767)
    PrivateFunction2('MinervaStand', 100)


@State
def ceef_hiteffD():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        Rotation(35000)
        Size(1200)
        RandAddScaleX(0, 250)
        RandAddRotation(-25000, 30000)
        RenderLayer(1)
        AlphaValue(200)
        BlendMode_Add()
    sprite('vr_mvcmneff_00', 4)
    CreateParticle('ceef_cmnHit01', -1)
    CreateObject('ceef_hiteffDSub', -1)
    sprite('vr_mvcmneff_01', 3)
    ConstantAlphaModifier(-8)
    sprite('vr_mvcmneff_02', 3)
    sprite('vr_mvcmneff_03', 3)
    sprite('vr_mvcmneff_04', 3)
    sprite('vr_mvcmneff_05', 3)
    sprite('vr_mvcmneff_07', 2)
    sprite('vr_mvcmneff_08', 2)


@State
def ceef_hiteffDSub():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        Rotation(90000)
        Size(1300)
        RandAddScaleX(0, 500)
        RandAddRotation(-15000, 15000)
        RenderLayer(1)
        AlphaValue(200)
        BlendMode_Add()
    sprite('vr_mvcmneff_00', 2)
    sprite('vr_mvcmneff_01', 2)
    sprite('vr_mvcmneff_02', 2)
    sprite('vr_mvcmneff_03', 2)
    sprite('vr_mvcmneff_04', 2)
    sprite('vr_mvcmneff_05', 2)
    sprite('vr_mvcmneff_07', 2)
    sprite('vr_mvcmneff_08', 2)


@State
def ceef_hiteffDSub2():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        Rotation(90000)
        SetScaleX(900)
        SetScaleY(1300)
        RandAddScaleX(0, 500)
        RandAddRotation(-15000, 15000)
        RenderLayer(1)
        BlendMode_Add()
        AlphaValue(180)
    sprite('vr_mvcmneff2_00', 2)
    CreateObject('ceef_hiteffDSub3', -1)
    sprite('vr_mvcmneff2_01', 2)
    sprite('vr_mvcmneff2_02', 2)
    sprite('vr_mvcmneff2_03', 2)
    sprite('vr_mvcmneff2_04', 2)
    sprite('vr_mvcmneff2_05', 2)
    sprite('vr_mvcmneff2_06', 3)
    sprite('vr_mvcmneff2_07', 3)
    sprite('vr_mvcmneff2_08', 2)


@State
def ceef_hiteffDSub3():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        SetScaleX(1600)
        SetScaleY(1800)
        RandAddScaleX(0, 250)
        RandAddRotation(-15000, 15000)
        RenderLayer(1)
        AlphaValue(180)
        BlendMode_Add()
    sprite('vr_mvcmneff2_00', 2)
    sprite('vr_mvcmneff2_01', 2)
    sprite('vr_mvcmneff2_02', 2)
    sprite('vr_mvcmneff2_03', 2)
    sprite('vr_mvcmneff2_04', 2)
    sprite('vr_mvcmneff2_05', 2)
    sprite('vr_mvcmneff2_06', 3)
    sprite('vr_mvcmneff2_07', 3)
    sprite('vr_mvcmneff2_08', 2)


@State
def ceef_hiteffH():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        Rotation(15000)
        Size(1300)
        RandAddScaleX(0, 250)
        RandAddRotation(-25000, 25000)
        RenderLayer(1)
        BlendMode_Add()
    sprite('vr_mvcmneff_00', 4)
    ParticleSize(1100)
    CallCustomizableParticle('ceef_cmnHit01', -1)
    CreateObject('ceef_hiteffDSub2', -1)
    sprite('vr_mvcmneff_01', 3)
    ConstantAlphaModifier(-8)
    CreateObject('ceef_hiteffHSub', -1)
    sprite('vr_mvcmneff_02', 3)
    sprite('vr_mvcmneff_03', 3)
    sprite('vr_mvcmneff_04', 3)
    sprite('vr_mvcmneff_05', 3)
    sprite('vr_mvcmneff_07', 2)
    sprite('vr_mvcmneff_08', 2)


@State
def ceef_hiteffHSub():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        Rotation(90000)
        Size(1600)
        RandAddScaleX(0, 500)
        RandAddRotation(-15000, 15000)
        RenderLayer(1)
        BlendMode_Add()
    sprite('vr_mvcmneff_00', 2)
    sprite('vr_mvcmneff_01', 2)
    sprite('vr_mvcmneff_02', 2)
    sprite('vr_mvcmneff_03', 2)
    sprite('vr_mvcmneff_04', 2)
    sprite('vr_mvcmneff_05', 2)
    sprite('vr_mvcmneff_07', 2)
    sprite('vr_mvcmneff_08', 2)


@State
def ceAirDashEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('ceef_airdash00')
        Eff3DEffect('ceef_airdash00.DIG', '')
        SetScaleX(400)
        SetScaleY(300)
        uponSendToLabel(32, 1)
    sprite('null', 5)
    AlphaValue(230)
    CreateObject('ceAirDashEffNokosi', -1)
    sprite('null', 5)


@State
def ceAirDashEffNokosi():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ceef_400eff01.DIG', '')
        SetScaleXPerFrame(30)
        Size(300)
        AlphaValue(128)
    sprite('null', 10)
    CreateParticle('ceef_airdash_nokosi2', -1)
    ConstantAlphaModifier(-17)


@State
def ceAirBDashEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('ceef_airdash00')
        Eff3DEffect('ceef_airdash01.DIG', '')
        SetScaleX(400)
        SetScaleY(300)
        uponSendToLabel(32, 1)
    sprite('null', 5)
    AlphaValue(230)
    CreateObject('ceAirDashEffNokosi', -1)
    sprite('null', 5)


@State
def mv202Eff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        ContinueState(20)
        PaletteIndex(1)
        RenderLayer(1)
        BlendMode_Normal()
        AlphaValue(200)
        Eff3DEffect('ceef_202eff00.DIG', '')
    label(0)
    sprite('mvef202eff_00', 3)
    CreateObject('mv213thunder', -1)

    def RunOnObject_1():
        AddY(250000)
        AddX(400000)
        Size(550)
    sprite('mvef202eff_01', 3)
    gotoLabel(0)


@State
def mv203Eff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        E0EAEffectPosition(2)
        Eff3DEffect('ceef_203eff00', '')
        BlendMode_Normal()
        SetScaleX(725)
        SetScaleY(650)
        AddX(25000)
        AddY(-25000)
        AlphaValue(210)
    sprite('null', 3)
    sprite('null', 5)
    Eff3DEffect('ceef_203eff01.DIG', '')
    ConstantAlphaModifier(-26)


@State
def mv204Smoke():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_cmnsmoke00', '')
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        AddX(10000)
        AlphaValue(255)
        SetScaleX(700)
        SetScaleY(450)
    sprite('null', 10)
    sprite('null', 12)
    ConstantAlphaModifier(-17)


@State
def mv204ringLoops():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        ContinueState(30)
    label(0)
    sprite('null', 2)
    CreateObject('mv204ring', -1)
    CreateParticle('ceef_kiramove00', -1)
    gotoLabel(0)


@State
def mv204ring():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(1)
        IgnoreScreenfreeze(1)
    sprite('vr_mvef204_00', 10)
    physicsXImpulse(-7500)
    SetScaleSpeed(60)
    ConstantAlphaModifier(-26)


@State
def mv205Eff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('ceef_205eff00', '')
        FaceSpawnLocation()
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        AddY(260000)
        AddX(-70000)
        AlphaValue(160)
        SetScaleX(800)
    sprite('null', 2)
    sprite('null', 8)


@State
def mv205ConsentEff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('ceef_205_plugeff_bigc')
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    CreateParticle('ceef_plugeff_cmnthunder', -1)
    ConstantAlphaModifier(-26)
    SetScaleSpeed(30)


@State
def mv211Eff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(192)
        PaletteColor1(161)
        PaletteColor3(162)
        PaletteColor4(1)
        AlphaValue(100)
        RenderLayer(1)
    sprite('vr_ce211_00', 3)
    sprite('vr_ce211_01', 2)
    sprite('vr_ce211_02', 10)
    ConstantAlphaModifier(-12)


@State
def mv212Eff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(192)
        PaletteColor1(193)
        PaletteColor3(194)
        PaletteColor4(1)
        AlphaValue(140)
        RenderLayer(1)
    sprite('vr_ce212_00', 3)
    sprite('vr_ce212_01', 10)
    ConstantAlphaModifier(-12)
    AddY(-60000)


@State
def mv232Eff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(192)
        PaletteColor1(193)
        PaletteColor3(194)
        PaletteColor4(1)
        AlphaValue(100)
        RenderLayer(1)
    sprite('vr_ce232_00', 3)
    sprite('vr_ce232_01', 3)
    sprite('vr_ce232_02', 10)
    ConstantAlphaModifier(-12)


@State
def mv233Eff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(3)
    sprite('null', 20)
    LinkParticle('ceef_233shock00')


@State
def mv236Eff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(192)
        PaletteColor1(193)
        PaletteColor3(194)
        PaletteColor4(1)
        AlphaValue(140)
        RenderLayer(1)
    sprite('vr_ce236_00', 3)
    sprite('vr_ce236_00', 10)
    ConstantAlphaModifier(-12)


@State
def mv252Eff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(192)
        PaletteColor1(193)
        PaletteColor3(194)
        PaletteColor4(1)
        AlphaValue(140)
        RenderLayer(1)
    sprite('vr_ce252_00', 3)
    sprite('vr_ce252_00', 10)
    ConstantAlphaModifier(-12)


@State
def mv251Eff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        IgnorePauses(3)
        BlendMode_Add()
        PaletteIndex(1)
        TurnParticleColorable1(1)
        PaletteEffType(2)
        PaletteColor2(192)
        PaletteColor1(193)
        PaletteColor3(194)
        PaletteColor4(1)
        AlphaValue(140)
        RenderLayer(1)
    sprite('vr_ce251_00', 3)
    sprite('vr_ce251_01', 3)
    sprite('vr_ce251_02', 10)
    ConstantAlphaModifier(-12)


@State
def mv213Eff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('ceef_213eff00', '')
        BlendMode_Normal()
        Size(700)
        AlphaValue(255)
        RotationAngle(-15000)
        AddY(100000)
    sprite('null', 3)
    CreateParticle('ceef_healsphere01', -1)
    CreateObject('mv213thunder', -1)
    sprite('null', 3)
    CreateObject('mv213thunder', -1)


@State
def mv213thunder():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_shoto_jizoku2', '')
        BlendMode_Normal()
        Size(700)
        AlphaValue(160)
        RandAddRotation(-100000, 100000)
    sprite('null', 15)


@State
def mv214Eff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('ceef_214eff00', '')
        BlendMode_Normal()
        Size(1050)
        AlphaValue(255)
        AddX(260000)
    sprite('null', 1)
    sprite('null', 2)
    CreateObject('mv214thunder', -1)

    def RunOnObject_1():
        Size(400)
        AddX(150000)
        AddY(150000)
    CreateObject('mv214thunder', -1)

    def RunOnObject_1():
        Size(600)
        AddX(150000)
        AddY(315000)
    CreateObject('mv214thunder', -1)

    def RunOnObject_1():
        Size(600)
        AddX(-30000)
        AddY(420000)
    CreateObject('mv214thunder', -1)

    def RunOnObject_1():
        Size(400)
        AddX(-240000)
        AddY(420000)
    sprite('null', 1)
    sprite('null', 3)
    Eff3DEffect('ceef_214eff01', '')
    ConstantAlphaModifier(-26)


@State
def mv214thunder():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_shoto_jizoku2b', '')
        BlendMode_Normal()
        Size(700)
        AlphaValue(160)
        RandAddRotation(-100000, 100000)
    sprite('null', 15)


@State
def ce215JetEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('ceef_400_shock')
        Eff3DEffect('ceef_400eff00.DIG', '')
        Size(600)
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 0)
    sprite('null', 5)
    CreateObject('ce215JetEffNokosi', -1)
    label(0)
    sprite('null', 5)
    CreateObject('ce215JetEffNokosi', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def ce215JetEffNokosi():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ceef_400eff01.DIG', '')
        AddX(100000)
        Size(300)
        physicsXImpulse(-7500)
    sprite('null', 10)
    CreateParticle('ceef_airdash_nokosi2', -1)
    ConstantAlphaModifier(-26)


@State
def mv215ConsentEff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        RotationAngle(90000)
        LinkParticle('ceef_208_plugeff_thunder')
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
    sprite('null', 32767)
    label(0)
    sprite('null', 32767)
    AddX(-7500)
    label(1)
    sprite('null', 5)
    CreateParticle('ceef_plugeff_cmnthunder', -1)
    ConstantAlphaModifier(-51)
    SetScaleSpeed(30)


@State
def mv234Eff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('ceef_234eff00', '')
        BlendMode_Normal()
        Size(4000)
        AddY(30000)
        AlphaValue(255)
    sprite('null', 2)
    sprite('null', 10)
    Eff3DEffect('ceef_234eff01', '')
    ConstantAlphaModifier(-26)


@State
def mv234ConsentEff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('ceef_208_plugeff_thunder')
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
        Rotation(180000)
    sprite('null', 32767)
    label(0)
    sprite('null', 32767)
    AddX(-50000)
    AddY(10000)
    label(1)
    sprite('null', 5)
    CreateParticle('ceef_plugeff_cmnthunder', -1)
    ConstantAlphaModifier(-51)
    SetScaleSpeed(30)


@State
def mv235Eff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('ceef_235eff00', '')
        BlendMode_Normal()
        Size(1600)
        AddY(1000)
        AlphaValue(255)
        AddX(180000)
    sprite('null', 4)
    LinkParticle('ceef_402_shock')
    CreateParticle('ceef_402_stone', -1)
    sprite('null', 4)
    Eff3DEffect('ceef_235eff01', '')
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def mv235ConsentEff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        RotationAngle(90000)
        LinkParticle('ceef_208_plugeff_thunder')
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
    sprite('null', 32767)
    label(0)
    sprite('null', 32767)
    AddX(-75000)
    label(1)
    sprite('null', 5)
    CreateParticle('ceef_plugeff_cmnthunder', -1)
    ConstantAlphaModifier(-51)
    SetScaleSpeed(30)


@State
def mv270Eff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        E0EAEffectPosition(2)
        Eff3DEffect('ceef_203eff00', '')
        BlendMode_Normal()
        SetScaleX(1100)
        SetScaleY(850)
        AddX(-60000)
        AddY(-20000)
        AlphaValue(200)
    sprite('null', 3)
    sprite('null', 5)
    AddX(-30000)
    Eff3DEffect('ceef_203eff01.DIG', '')
    ConstantAlphaModifier(-26)


@State
def mv311Eff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ceef_311eff00.DIG', '')
        IgnorePauses(2)
        CancelIfPlayerHit(3)
        Rotation(-30000)
        Size(4000)
        AddX(50000)
        AddY(325000)
        IgnoreScreenfreeze(1)
    sprite('null', 1)
    CreateObject('mv311wind', -1)
    PrivateSE('cese_12')
    PrivateSE('cese_08')
    sprite('null', 1)
    CreateObject('mv311ThunderEff', -1)
    CreateObject('mv311ThunderEff2', -1)
    CreateObject('mv311thunder', -1)

    def RunOnObject_1():
        AddX(150000)
        AddY(75000)
    CommonSE('014_electric_sl')
    CreateObject('mv311thunder2', -1)

    def RunOnObject_1():
        AddX(300000)
        AddY(150000)
    CreateObject('mv311thunder', -1)

    def RunOnObject_1():
        AddX(450000)
        AddY(225000)
    CreateObject('mv311thunder2', -1)

    def RunOnObject_1():
        AddX(600000)
        AddY(300000)
    sprite('null', 5)
    CreateObject('mv311thunder', -1)
    CreateObject('mv311BeamEnd', -1)
    ScreenShake(10000, 10000)
    SetScaleSpeedY(-350)
    SetScaleXPerFrame(-300)


@State
def mv311ThunderEff():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Add()
        Rotation(-145000)
        SetScaleX(1250)
        SetScaleY(1500)
        RandAddScaleY(500, 2000)
        RandAddScaleX(0, 500)
        SetZVal(-1000)
        IgnoreScreenfreeze(1)
    sprite('vr_mvef403a_00', 2)
    CommonSE('014_electric_s')
    sprite('null', 1)
    sprite('vr_mvef403a_01', 2)
    CommonSE('014_electric_l')
    sprite('null', 1)
    sprite('vr_mvef403a_02', 2)
    CommonSE('014_electric_m')
    sprite('vr_mvef403a_03', 2)


@State
def mv311ThunderEff2():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Add()
        Rotation(-85000)
        SetScaleX(1250)
        SetScaleY(1500)
        RandAddScaleY(500, 2000)
        RandAddScaleX(0, 500)
        SetZVal(-500)
        IgnoreScreenfreeze(1)
    sprite('vr_mvef403a_00', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_01', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_02', 2)
    sprite('vr_mvef403a_03', 2)


@State
def mv311thunder():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_shoto_jizoku2b', '')
        BlendMode_Normal()
        Size(700)
        RandAddRotation(-100000, 100000)
        IgnoreScreenfreeze(1)
    sprite('null', 6)
    AlphaValue(0)
    SetScaleSpeed(15)
    sprite('null', 9)
    AlphaValue(255)
    CreateParticle('ceef_healsphere01', -1)


@State
def mv311thunder2():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_shoto_jizoku2', '')
        BlendMode_Normal()
        Size(450)
        RandAddRotation(-100000, 100000)
        IgnoreScreenfreeze(1)
    sprite('null', 6)
    AlphaValue(0)
    sprite('null', 9)
    AlphaValue(255)
    CreateParticle('ceef_healsphere01', -1)


@State
def mv311BeamEnd():

    def upon_IMMEDIATE():
        LinkParticle('ceef_311beamend00')
        Rotation(-30000)
        IgnoreScreenfreeze(1)
    sprite('null', 60)


@State
def mv311wind():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_cmnsmoke00', '')
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        AddX(-25000)
        AddY(-325000)
        AlphaValue(255)
        SetScaleX(750)
        SetScaleY(550)
    sprite('null', 22)
    SetScaleSpeed(5)
    ConstantAlphaModifier(-5)


@State
def mv311ConsentEff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        RotationAngle(180000)
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 2)
    sprite('null', 32767)
    CreateParticle('ceef_311__plugeff_sc', -1)
    label(1)
    sprite('null', 32767)
    LinkParticle('ceef_205_plugeff_bigc')
    label(2)
    sprite('null', 5)
    CreateParticle('ceef_plugeff_cmnthunder', -1)
    ConstantAlphaModifier(-51)
    SetScaleSpeed(30)
    loopRest()


@State
def mv321BomEff():

    def upon_IMMEDIATE():
        Eff3DEffect('ceeff_cmnbomb00', '')
        BlendMode_Normal()
        TeleportToObject(22)
        AddY(300000)
        AddX(150000)
        SetScaleY(1000)
        SetScaleX(800)
        Rotation(20000)
        IgnoreScreenfreeze(1)
        RenderLayer(1)
    sprite('null', 3)
    sprite('null', 3)
    CreateParticle('ceef_321_fallfireball00', -1)
    CreateParticle('ceef_321_fallfireball01', -1)
    CreateParticle('ceef_321_fallfireball02', -1)
    AddScale(250)
    sprite('null', 3)
    AddScale(150)
    CreateParticle('ceef_321_bloom', -1)
    ScreenShake(15000, 15000)
    sprite('null', 9)
    AddScale(100)


@State
def mv340ConsentEff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('ceef_208_plugeff_thunder')
        uponSendToLabel(32, 1)
    sprite('null', 32767)
    label(1)
    sprite('null', 5)
    CreateParticle('ceef_plugeff_cmnthunder', -1)
    ConstantAlphaModifier(-51)
    SetScaleSpeed(30)


@State
def ceef_270():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        LinkParticle('ceef_270ring')
    sprite('null', 60)


@State
def ce400JetEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(2)
        LinkParticle('ceef_400_shock')
        Eff3DEffect('ceef_400eff00.DIG', '')
        Size(750)
        uponSendToLabel(32, 1)
    sprite('null', 4)
    CreateObject('ce400JetEffNokosi', -1)
    sprite('null', 1)
    label(0)
    sprite('null', 5)
    CreateObject('ce400JetEffNokosi', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    loopRest()


@State
def ce400JetEffBackFireAtk():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(200)
        AttackP2(101)
        Hitstop(0)
        AirPushbackX(120000)
        AirPushbackY(-100000)
        HardKnockdown(1)
        HitsparkSize(500)
        VoodooDamageMultiplier(2)
        Unknown12052(1)
        DamageFromStateOnly('ce400JetEffBackFireAtk')
        DistanceCheck(100000, -1000000, -1, -1)
        AirUntechableTime(40)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        UseFireHitspark(1)
        VoodooDamageMultiplier(3)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        uponSendToLabel(33, 1)
    sprite('null', 2)
    label(0)
    sprite('ce400_dummyAtk', 2)
    RefreshMultihit()
    gotoLabel(0)
    label(1)
    sprite('ce400_dummyAtk', 3)
    RefreshMultihit()
    AttackLevel_(4)
    AirPushbackX(5000)
    AirPushbackY(32000)
    DamageFromStateOnly('')
    HardKnockdown(0)


@State
def ce400JetEffNokosi():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ceef_400eff01.DIG', '')
        AddX(100000)
        Size(600)
        physicsXImpulse(-7500)
    sprite('null', 10)
    CreateParticle('ceef_airdash_nokosi2', -1)
    ConstantAlphaModifier(-26)


@State
def mv400tameMatome():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        BlendMode_Normal()
        AddY(150000)
        AddX(10000)
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 7)
    CreateObject('mv400tame', -1)
    ParticleSize(800)
    CallCustomizableParticle('ceef_400tame_pos', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 7)
    CreateObject('mv400tame', -1)
    ParticleSize(800)
    CallCustomizableParticle('ceef_400tame_pos', -1)
    sprite('null', 7)
    ParticleSize(800)
    CallCustomizableParticle('ceef_400tame_pos', -1)


@State
def mv400tame():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_shoto_jizoku2b', '')
        BlendMode_Normal()
        Size(1300)
        RandAddRotation(-100000, 100000)
    sprite('null', 15)


@State
def mv400windMatome():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    label(0)
    sprite('null', 5)
    CreateParticle('ceef_cmn_stone00', -1)
    CreateObject('mv400wind', -1)
    sprite('null', 5)
    CreateParticle('ceef_cmn_stone00', -1)
    gotoLabel(0)


@State
def mv400wind():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_cmnsmoke01', '')
        BlendMode_Normal()
        AddX(10000)
        AlphaValue(255)
        SetScaleX(700)
        SetScaleY(450)
        physicsXImpulse(-3500)
        SetScaleSpeed(30)
        RandAddScaleY(-150, 0)
    sprite('null', 10)
    sprite('null', 12)
    ConstantAlphaModifier(-21)


@State
def AssaultPlug():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 2)
        RenderLayer(11)
        SetZVal(100)
        AddX(5000)
    sprite('vr_ce215_00', 32767)
    loopRest()
    label(1)
    sprite('vr_ce215_01', 32767)
    loopRest()
    label(2)
    sprite('vr_ce215_03', 10)
    ConstantAlphaModifier(-25)
    loopRest()


@State
def Cable():

    def upon_IMMEDIATE():
        WallCollisionDetection(1)
        FloorCollision(1)
        SetXCollisionFromOrigin(10)
        IgnorePauses(3)
        ContinueState(240)
        SetActionMark(0)
        RotationSomething(0)
        CopyFromRightToLeft(1, 2, 1, 23, 2, 1)
        SLOT_57 = 109
        AddX(-240000)
        AddY(-21000)

        def upon_31():
            CallPrivateFunction('CableDraw', 0, 0, 0, 0, 0, 0, 0, 0)
        CallPrivateFunction('Cablejoint', 0, 4, 0, 0, 0, 0, 0, 0)
        RenderLayer(0)
        CallPrivateFunction('CableRenderStage', 0, 11, 0, 11, 0, 0, 0, 0)

        def upon_48():
            CallPrivateFunction('CableIdling', 0, 0, 0, 0, 0, 0, 0, 0)
        SLOT_54 = 1

        def upon_EVERY_FRAME():
            if SLOT_51:
                CallPrivateFunction('CableAngleByChain', 0, 0, 0, 0, 0, 0, 0, 0
                    )
            if SLOT_54:
                RotationSomething(0)
            CopyFromRightToLeft(23, 2, 52, 3, 2, 51)
            if not SLOT_52:
                if not SLOT_53:
                    DeleteObject(23)

        def upon_32():
            clearUponHandler(32)
            TeleportToObject(4)
            AddY(120000)
            sendToLabel(100)
    sprite('null', 1)
    CallPrivateFunction('CableParam', 0, 0, 0, 7770, 0, 0, 0, 0)
    CallPrivateFunction('CableParam', 0, 1, 0, 33, 0, 0, 0, 10)
    CallPrivateFunction('CableParam', 0, 2, 0, 66, 0, 0, 0, 10)
    CallPrivateFunction('CableParam', 0, 3, 0, 7771, 0, 0, 0, 0)
    CallPrivateFunction('CableSpeed', 0, 3000, 0, 0, 0, 0, 0, 0)
    CallPrivateFunction('CableFirstPosition', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('null', 32767)
    loopRest()
    label(100)
    sprite('vr_ce215_02', 30)
    RenderLayer(0)
    SetZVal(100)
    clearUponHandler(41)
    Unknown23143(90000, 0, 80)
    SLOT_51 = 1
    SLOT_54 = 0
    loopRest()
    ExitState()


@State
def EntryCelicaDummy():

    def upon_IMMEDIATE():

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)

        def upon_33():
            clearUponHandler(33)
            sendToLabel(2)
    sprite('ce602_00', 6)
    XPositionRelativeFacing(-800000)
    physicsXImpulse(14000)
    sprite('ce602_01', 6)
    sprite('ce602_02', 6)
    sprite('ce602_03', 6)
    DashEffects(100, 1, 1)
    sprite('ce602_04', 6)
    sprite('ce602_05', 6)
    label(0)
    sprite('ce602_00', 6)
    sprite('ce602_01', 6)
    sprite('ce602_02', 6)
    sprite('ce602_03', 6)
    DashEffects(100, 1, 1)
    sprite('ce602_04', 6)
    sprite('ce602_05', 6)
    gotoLabel(0)
    label(1)
    sprite('ce602_06', 7)
    XPositionRelativeFacing(-240000)
    physicsXImpulse(-2000)
    sprite('ce602_07', 7)
    CommonSE('019_cloth_a')
    sprite('ce602_08', 8)
    physicsXImpulse(-1000)
    CommonSE('019_cloth_a')
    sprite('ce602_09', 20)
    physicsXImpulse(0)
    XPositionRelativeFacing(-260000)
    ScreenCollision(0)
    sprite('ce602_10', 7)
    sprite('ce602_11', 10)
    sprite('ce602_11', 32767)
    label(2)
    sprite('null', 5)
    loopRest()


@State
def EntryCable():

    def upon_IMMEDIATE():
        WallCollisionDetection(1)
        FloorCollision(1)
        SetXCollisionFromOrigin(10)
        IgnorePauses(3)
        ContinueState(600)
        SLOT_51 = 1
        SLOT_54 = 0
        physicsXImpulse(70000)
        SetActionMark(0)
        RotationSomething(0)
        CopyFromRightToLeft(1, 2, 1, 23, 2, 1)

        def upon_31():
            CallPrivateFunction('CableDraw', 0, 0, 0, 0, 0, 0, 0, 0)
        CallPrivateFunction('Cablejoint', 0, 4, 0, 0, 0, 0, 0, 0)
        RenderLayer(11)
        CallPrivateFunction('CableRenderStage', 0, 12, 0, 13, 0, 0, 0, 0)

        def upon_48():
            CallPrivateFunction('CableIdling', 0, 0, 0, 0, 0, 0, 0, 0)
        SLOT_54 = 1

        def upon_EVERY_FRAME():
            if SLOT_51:
                CallPrivateFunction('CableAngleByChain', 0, 0, 0, 0, 0, 0, 0, 0
                    )
            if SLOT_54:
                RotationSomething(0)
            CopyFromRightToLeft(23, 2, 52, 3, 2, 51)
            if not SLOT_52:
                if not SLOT_53:
                    DeleteObject(23)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(100)
    sprite('null', 1)
    CallPrivateFunction('CableParam', 0, 0, 0, 7770, 0, 0, 0, 0)
    CallPrivateFunction('CableParam', 0, 1, 0, 33, 0, 0, 0, 10)
    CallPrivateFunction('CableParam', 0, 2, 0, 66, 0, 0, 0, 10)
    CallPrivateFunction('CableParam', 0, 3, 0, 7771, 0, 0, 0, 0)
    CallPrivateFunction('CableSpeed', 0, 3000, 0, 0, 0, 0, 0, 0)
    CallPrivateFunction('CableFirstPosition', 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('vr_ce215_02', 32767)
    loopRest()
    label(100)
    sprite('vr_ce215_02', 2)
    XImpulseAcceleration(5)
    sprite('null', 32767)
    physicsXImpulse(0)
    AddX(-150000)
    loopRest()
    ExitState()


@State
def ce401PanchEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        E0EAEffectPosition(2)
        Eff3DEffect('ceef_401eff00.DIG', '')
        AddY(400000)
        AddX(-2000)
        Size(1000)
    sprite('null', 5)
    CreateParticle('ceef_401panch', -1)
    CreateObject('mv401Nokosi', -1)
    CreateObject('mv401Nokosi2', -1)
    sprite('null', 5)
    AddX(-50000)


@State
def mv401Nokosi():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_shoto_jizoku2', '')
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        BlendMode_Normal()
        RandAddRotation(-100000, 100000)
        DeviationY(0, 15000)
        DeviationX(100000, 100000)
        Size(1000)
    sprite('null', 10)
    sprite('null', 5)


@State
def mv401Nokosi2():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_shoto_jizoku2b', '')
        BlendMode_Normal()
        RandAddRotation(-100000, 100000)
        DeviationY(-170000, -170000)
        DeviationX(-10000, -10000)
        Size(800)
    sprite('null', 10)
    sprite('null', 5)


@State
def mv401tameMatome():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        BlendMode_Normal()
        AddY(300000)
        AddX(10000)
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 7)
    CreateObject('mv401tame', -1)
    CreateParticle('ceef_401tame_sub', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 7)
    CreateObject('mv401tame', -1)
    CreateParticle('ceef_401tame_sub', -1)
    sprite('null', 7)
    CreateParticle('ceef_401tame_sub', -1)


@State
def mv401tame():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_shoto_jizoku2b', '')
        BlendMode_Normal()
        Size(800)
        RandAddRotation(-100000, 100000)
    sprite('null', 15)


@State
def mv402Eff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        Eff3DEffect('ceef_402eff00', '')
        BlendMode_Normal()
        AddX(130000)
        AddY(-20000)
        Size(1600)
        Flip()
    sprite('null', 4)
    LinkParticle('ceef_402_shock')
    CreateObject('mv402Nokosi2', -1)

    def RunOnObject_1():
        AddX(-100000)
    CreateObject('mv402Nokosi2', -1)

    def RunOnObject_1():
        AddX(200000)
    CreateObject('mv402wind', -1)
    CreateObject('mv402Nokosi', -1)

    def RunOnObject_1():
        AddY(50000)
        AlphaValue(175)
    CreateObject('mv402Nokosi', -1)

    def RunOnObject_1():
        Size(600)
        AddY(200000)
        AddX(150000)
        AlphaValue(175)
    CreateObject('mv402Nokosi', -1)

    def RunOnObject_1():
        Size(450)
        AddY(200000)
        AddX(300000)
        AlphaValue(175)
    sprite('null', 4)
    Eff3DEffect('ceef_402eff01', '')
    sprite('null', 6)
    ConstantAlphaModifier(-51)


@State
def mv402Nokosi():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_shoto_jizoku2b', '')
        BlendMode_Normal()
        RandAddRotation(-100000, 100000)
        DeviationY(300000, 300000)
        Size(1000)
    sprite('null', 5)
    AlphaValue(0)
    sprite('null', 9)
    AlphaValue(255)


@State
def mv402Nokosi2():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_shoto_jizoku2b', '')
        BlendMode_Normal()
        RandAddRotation(-100000, 100000)
        DeviationY(100000, 100000)
        DeviationX(-100000, -100000)
        Size(1000)
    sprite('null', 15)
    AlphaValue(255)


@State
def mv402tameMatome():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        BlendMode_Normal()
        AddY(40000)
        AddX(-150000)
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 7)
    CreateObject('mv402tame', -1)
    CreateParticle('ceef_402tame_bloom', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 7)
    CreateObject('mv402tame', -1)
    CreateParticle('ceef_402tame_bloom', -1)
    sprite('null', 7)
    CreateParticle('ceef_402tame_bloom', -1)


@State
def mv402tame():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_shoto_jizoku2', '')
        BlendMode_Normal()
        Size(1300)
        RandAddRotation(-100000, 100000)
        RenderLayer(2)
    sprite('null', 15)


@State
def mv402wind():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_cmnsmoke00', '')
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        AddX(10000)
        AlphaValue(255)
        SetScaleX(-700)
        SetScaleY(450)
    sprite('null', 10)
    sprite('null', 12)
    ConstantAlphaModifier(-17)


@State
def ce404StarEff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        Flip()
        RenderLayer(1)
    sprite('vr_mvef404_00', 5)
    CreateObject('ceef_404StarSub', -1)
    SetScaleSpeed(80)
    CreateParticle('ceef_kickhiteff00', -1)
    sprite('vr_mvef404_00', 10)
    ConstantAlphaModifier(-26)
    SetScaleSpeed(30)


@State
def ce404KickEff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        Eff3DEffect('ceef_kickeff00', '')
        LinkParticle('ceef_404kickjizoku00')
        BlendMode_Normal()
        RotationAngle(-40000)
        AddX(90000)
        SetScaleX(1500)
        SetScaleY(3000)
        uponSendToLabel(32, 1)
    sprite('null', 1)
    CreateParticle('ceef_kickeff01', -1)
    CreateParticle('ceef_kickstart', -1)
    label(0)
    sprite('null', 5)
    CreateParticle('ceef_kickeff01', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    SetScaleXPerFrame(-120)
    SetScaleSpeedY(120)
    ConstantAlphaModifier(-26)
    loopRest()


@State
def ceef_404StarSub():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        Rotation(20000)
        Size(1300)
        RandAddScaleX(0, 250)
        RandAddRotation(-15000, 15000)
        RenderLayer(1)
        BlendMode_Add()
    sprite('vr_mvcmneff_00', 4)
    sprite('vr_mvcmneff_01', 3)
    ConstantAlphaModifier(-8)
    sprite('vr_mvcmneff_02', 3)
    sprite('vr_mvcmneff_03', 3)
    sprite('vr_mvcmneff_04', 3)
    sprite('vr_mvcmneff_05', 3)
    sprite('vr_mvcmneff_07', 2)
    sprite('vr_mvcmneff_08', 2)


@State
def mv403ShotEff():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_shoto_jizoku', '')
        FaceSpawnLocation()
        BlendMode_Normal()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        AddY(75000)
        uponSendToLabel(32, 1)
    sprite('null', 15)
    Size(100)
    SetScaleSpeed(60)
    label(0)
    sprite('null', 3)
    SetScaleSpeed(0)
    CreateObject('mv403Nokosi', 100)
    CreateObject('mv403Nokosi2', 100)
    CreateObject('mv403Nokosi3', 100)
    sprite('null', 3)
    CreateObject('mv403Nokosi3', 100)
    gotoLabel(0)
    label(1)
    sprite('null', 3)
    CreateParticle('ceef_shotbrake00', -1)
    loopRest()


@State
def mv403Nokosi():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_cmnparticle00', '')
        BlendMode_Normal()
        Size(30)
        RandAddRotation(-10000, 10000)
        DeviationY(-150000, 150000)
        IgnoreScreenfreeze(1)
    sprite('null', 10)
    SetScaleSpeed(50)
    CreateParticle('ceef_shot_01', -1)
    sprite('null', 10)
    SetScaleSpeed(-10)
    sprite('null', 25)
    ConstantAlphaModifier(-10)


@State
def mv403Nokosi2():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_cmnparticle01', '')
        BlendMode_Add()
        Size(30)
        RandAddRotation(-10000, 10000)
        DeviationY(-150000, 150000)
        IgnoreScreenfreeze(1)
    sprite('null', 10)
    SetScaleSpeed(50)
    CreateParticle('ceef_shot_01', -1)
    sprite('null', 10)
    SetScaleSpeed(-10)
    sprite('null', 25)
    ConstantAlphaModifier(-10)


@State
def mv403Nokosi3():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_shoto_jizoku2', '')
        BlendMode_Normal()
        RandAddRotation(-100000, 100000)
        Size(600)
    sprite('null', 14)
    ConstantAlphaModifier(-7)
    SetScaleSpeed(-7)
    physicsXImpulse(-6000)


@State
def mv403Nokosistart():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_shotstart00', '')
        BlendMode_Normal()
        Size(800)
        AddY(80000)
    sprite('null', 5)
    CreateObject('mv403Impact', 100)
    CreateObject('mv403Impact2', 100)
    SetScaleSpeed(300)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    SetScaleSpeed(30)


@State
def mv403Impact():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_windanim00', '')
        BlendMode_Normal()
        AddX(-100000)
        SetScaleY(1250)
        SetScaleX(2000)
        AlphaValue(255)
    sprite('null', 5)
    SetScaleSpeed(15)
    physicsXImpulse(-15000)
    sprite('null', 5)
    ConstantAlphaModifier(-17)


@State
def mv403Impact2():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_windanim00', '')
        BlendMode_Normal()
        AddX(-75000)
        SetScaleY(1000)
        SetScaleX(1800)
        AlphaValue(255)
    sprite('null', 5)
    sprite('null', 5)
    ConstantAlphaModifier(-17)


@State
def mv403ConsentEff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('ceef_208_plugeff_thunder')
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    CreateParticle('ceef_plugeff_cmnthunder', -1)
    ConstantAlphaModifier(-26)
    SetScaleSpeed(30)


@State
def mv403Eff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        SetZVal(-500)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('vr_mvef403_00', 1)
    CreateObject('mv403EffParticle', 0)
    CreateObject('mv403SubEff', 100)
    CreateObject('mv403mazleEff', 100)
    CreateObject('mv403mazleEff2', 100)
    CreateObject('mv403mazleEff3', 100)
    PrivateSE('cese_12')
    label(1)
    sprite('vr_mvef403_00', 2)
    CreateObject('mv403ThunderEff', -1)
    CreateObject('mv403ThunderEff2', -1)
    CreateObject('mv403BeamEff', -1)
    CreateObject('mv403BeamEff2', -1)
    CreateObject('mv403Smoke', 100)
    CreateObject('mvBeamNokosi', 1)
    CreateObject('mvBeamNokosi2', 1)
    CreateObject('mvBeamNokosi', 2)
    CreateObject('mvBeamNokosi2', 2)
    CreateObject('mvBeamNokosi', 3)
    CreateObject('mvBeamNokosi2', 3)
    CreateObject('mvBeamNokosi', 4)
    CreateObject('mvBeamNokosi2', 4)
    CreateObject('mvBeamNokosi', 5)
    CreateObject('mvBeamNokosi2', 5)
    PrivateSE('cese_12')
    sprite('vr_mvef403_01', 2)
    CreateObject('mv403BeamEff', -1)
    CreateObject('mv403BeamEff2', -1)
    PrivateSE('cese_12')
    sprite('vr_mvef403_02', 2)
    PrivateSE('cese_12')
    gotoLabel(1)


@State
def mv403BeamEff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        Eff3DEffect('ceef_beamEff00.DIG', '')
        AddY(300000)
        AddX(300000)
        Size(1300)
        BlendMode_Normal()
        DeviationY(-25000, 25000)
        DeviationX(0, 500000)
    sprite('null', 1)
    sprite('null', 1)
    AlphaValue(128)


@State
def mv403BeamEff2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        Eff3DEffect('ceef_beamEff00.DIG', '')
        AddY(300000)
        AddX(300000)
        Size(1300)
        BlendMode_Normal()
        DeviationY(-25000, 25000)
        DeviationX(500000, 1250000)
    sprite('null', 1)
    sprite('null', 1)
    AlphaValue(128)


@State
def mvBeamNokosi():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_cmnparticle00', '')
        BlendMode_Normal()
        Size(500)
        RandAddRotation(-10000, 10000)
        DeviationY(75000, 150000)
        DeviationX(-150000, 150000)
        IgnoreScreenfreeze(1)
    sprite('null', 10)
    SetScaleSpeed(-30)
    ConstantAlphaModifier(-26)


@State
def mvBeamNokosi2():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_cmnparticle01', '')
        BlendMode_Add()
        Size(500)
        RandAddRotation(-10000, 10000)
        DeviationY(-170000, -100000)
        DeviationX(-150000, 150000)
        IgnoreScreenfreeze(1)
    sprite('null', 10)
    SetScaleSpeed(-30)
    ConstantAlphaModifier(-26)


@State
def mvBeamNokosi3():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_shoto_jizoku2', '')
        BlendMode_Normal()
        RandAddRotation(-100000, 100000)
        DeviationY(0, 150000)
        DeviationX(-150000, 150000)
        Size(600)
    sprite('null', 14)
    ConstantAlphaModifier(-7)
    SetScaleSpeed(-7)
    physicsXImpulse(-6000)


@State
def mv403EffParticle():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
    sprite('null', 32767)
    LinkParticle('ceef_ddlaser_00')


@State
def mv403SubEff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        SetZVal(-500)
        IgnoreScreenfreeze(1)
        BlendMode_Sub()
    sprite('null', 1)
    label(0)
    sprite('vr_mvef403sub_00', 2)
    CreateObject('mv403BulletEff', 100)
    CreateObject('mv403BulletEff2', 100)
    sprite('vr_mvef403sub_01', 2)
    sprite('vr_mvef403sub_02', 2)
    CreateObject('mv403BulletEff', 100)
    CreateObject('mv403BulletEff2', 100)
    gotoLabel(0)


@State
def mv403BulletEff():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        SetZVal(-500)
        IgnoreScreenfreeze(1)
        AddY(80000)
        AddX(250000)
        DeviationY(-40000, 40000)
        Size(-600)
        EnableAfterimage(1)
        AfterimageCount(5)
    sprite('vr_mvef403_03', 30)
    physicsXImpulse(70000)
    SetScaleXPerFrame(-100)


@State
def mv403BulletEff2():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        SetZVal(-1000)
        IgnoreScreenfreeze(1)
        AddY(350000)
        AddX(200000)
        DeviationY(-60000, 60000)
        Size(-1000)
        EnableAfterimage(1)
        AfterimageCount(5)
        BlendMode_Normal()
    sprite('vr_mvef403_03', 30)
    physicsXImpulse(70000)
    SetScaleXPerFrame(-75)


@State
def mv403mazleEff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        SetZVal(-500)
        IgnoreScreenfreeze(1)
        AddY(90000)
        AddX(270000)
    label(0)
    sprite('vr_mvef403mzl_00', 2)
    sprite('vr_mvef403mzl_01', 2)
    gotoLabel(0)


@State
def mv403mazleEff2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        SetZVal(-500)
        IgnoreScreenfreeze(1)
        AddY(360000)
        AddX(230000)
        Size(600)
        BlendMode_Add()
        AlphaValue(180)
    label(0)
    sprite('vr_mvef403mzl_00', 2)
    sprite('vr_mvef403mzl_01', 2)
    gotoLabel(0)


@State
def mv403mazleEff3():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        SetZVal(1000)
        IgnoreScreenfreeze(1)
        AddY(370000)
        AddX(250000)
        Size(600)
    label(0)
    sprite('vr_mvef403mzl_00', 2)
    sprite('vr_mvef403mzl_01', 2)
    gotoLabel(0)


@State
def mv403EffOD():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        PaletteIndex(1)
        SetZVal(-500)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 2)
    sprite('null', 32767)
    label(0)
    sprite('vr_mvef403_00od', 1)
    CreateObject('mv403EffAddPartsOD', -1)
    CreateObject('mv403EffParticleOD', 0)
    CreateObject('mv403SubEff', 100)
    CreateObject('mv403mazleEff', 100)

    def RunOnObject_1():
        AddScale(300)
    CreateObject('mv403mazleEff2', 100)
    CreateObject('mv403mazleEff3', 100)
    PrivateSE('cese_12')
    label(1)
    sprite('vr_mvef403_00od', 2)
    ScreenShake(1000, 1000)
    CreateObject('mv403ThunderEff', -1)
    CreateObject('mv403ThunderEff2', -1)
    CreateObject('mv403Smoke', 100)
    CreateObject('mvBeamNokosi', 1)

    def RunOnObject_1():
        AddY(50000)
    CreateObject('mvBeamNokosi2', 1)

    def RunOnObject_1():
        AddY(-50000)
    CreateObject('mvBeamNokosi', 2)

    def RunOnObject_1():
        AddY(50000)
    CreateObject('mvBeamNokosi2', 2)

    def RunOnObject_1():
        AddY(-50000)
    CreateObject('mvBeamNokosi', 3)

    def RunOnObject_1():
        AddY(50000)
    CreateObject('mvBeamNokosi2', 3)

    def RunOnObject_1():
        AddY(-50000)
    CreateObject('mvBeamNokosi', 4)

    def RunOnObject_1():
        AddY(50000)
    CreateObject('mvBeamNokosi2', 4)

    def RunOnObject_1():
        AddY(-50000)
    CreateObject('mvBeamNokosi', 5)

    def RunOnObject_1():
        AddY(50000)
    CreateObject('mvBeamNokosi2', 5)

    def RunOnObject_1():
        AddY(-50000)
    PrivateSE('cese_12')
    sprite('vr_mvef403_01od', 2)
    ScreenShake(1000, 1000)
    PrivateSE('cese_12')
    sprite('vr_mvef403_02od', 2)
    ScreenShake(1000, 1000)
    PrivateSE('cese_12')
    gotoLabel(1)
    label(2)
    sprite('vr_mvef403_00od', 2)
    ConstantAlphaModifier(-51)
    TriggerUponForState('mv403EffAddPartsOD', 32)
    DespawnEAEffect('mv403EffParticleOD')
    DespawnEAEffect('mv403SubEff')
    DespawnEAEffect('mv403mazleEff')
    DespawnEAEffect('mv403mazleEff2')
    DespawnEAEffect('mv403mazleEff3')
    PrivateSE('cese_12')
    sprite('vr_mvef403_01od', 2)
    PrivateSE('cese_12')
    sprite('vr_mvef403_02od', 15)
    CreateObject('mvBeamNokosi', 1)
    CreateObject('mvBeamNokosi2', 1)
    CreateObject('mvBeamNokosi', 2)
    CreateObject('mvBeamNokosi2', 2)
    CreateObject('mvBeamNokosi', 3)
    CreateObject('mvBeamNokosi2', 3)
    CreateObject('mvBeamNokosi', 4)
    CreateObject('mvBeamNokosi2', 4)
    CreateObject('mvBeamNokosi', 5)
    CreateObject('mvBeamNokosi2', 5)
    DespawnEAEffect('mv403ThunderEff')
    DespawnEAEffect('mv403ThunderEff2')
    PrivateSE('cese_12')


@State
def mv403EffParticleOD():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
    sprite('null', 32767)
    LinkParticle('ceef_ddlaserod_00')


@State
def mv403EffAddPartsOD():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        BlendMode_Normal()
        AddY(275000)
        AddX(300000)
        SetScaleX(2000)
        SetScaleY(2500)
        AddAlpha(128)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    Eff3DEffect('ceef_403odbeam00', '')
    label(0)
    sprite('null', 10)
    SetScaleSpeedY(-80)
    ConstantAlphaModifier(-26)


@State
def mv403TameEffOD():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        IgnoreScreenfreeze(1)
        LinkParticle('ceef_tamebeam_00')
        uponSendToLabel(32, 1)

        def upon_EVERY_FRAME():
            PrivateFunction3(2, 450000, 250000, 100, 0)
    label(0)
    sprite('null', 3)
    Size(1500)
    ScreenShake(2500, 2500)
    RandAddRotation(0, 100000)
    sprite('null', 3)
    RandAddScaleX(0, 250)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    ScreenShake(20000, 20000)
    CreateParticle('ceef_tamebeam_end', -1)
    CreateParticle('ceef_beamstart00', -1)


@State
def mv403TameEff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        IgnoreScreenfreeze(1)
        LinkParticle('ceef_tamebeam_00')
        uponSendToLabel(32, 1)

        def upon_EVERY_FRAME():
            PrivateFunction3(2, 450000, 250000, 100, 0)
    label(0)
    sprite('null', 3)
    Size(1200)
    ScreenShake(2500, 2500)
    RandAddRotation(0, 100000)
    sprite('null', 3)
    RandAddScaleX(0, 250)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    ScreenShake(20000, 20000)
    CreateParticle('ceef_tamebeam_end', -1)
    CreateParticle('ceef_beamstart00', -1)


@State
def mv403TameEffSub():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        IgnoreScreenfreeze(1)
        SetZVal(-500)

        def upon_EVERY_FRAME():
            PrivateFunction3(2, 0, -30000, 100, 0)
    sprite('null', 8)
    sprite('vr_mvef403s_00', 4)
    sprite('vr_mvef403s_01', 4)
    sprite('vr_mvef403s_02', 3)
    sprite('vr_mvef403s_03', 3)
    sprite('vr_mvef403s_04', 2)
    sprite('vr_mvef403s_05', 2)
    sprite('vr_mvef403s_06', 2)
    label(0)
    sprite('vr_mvef403s_03', 2)
    sprite('vr_mvef403s_04', 2)
    sprite('vr_mvef403s_05', 2)
    sprite('vr_mvef403s_06', 2)
    sprite('null', 3)
    gotoLabel(0)


@State
def mv403ThunderEff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        RandAddRotation(-60000, 100000)
        SetScaleX(1250)
        SetScaleY(1500)
        RandAddScaleY(500, 2000)
        RandAddScaleX(0, 500)
        SetZVal(-500)
        AddY(250000)
        AddX(300000)
    sprite('vr_mvef403a_00', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_01', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_02', 2)
    sprite('vr_mvef403a_03', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_00', 2)
    sprite('vr_mvef403a_01', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_02', 2)
    sprite('vr_mvef403a_03', 2)


@State
def mv403ThunderEff2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        RandAddRotation(100000, 250000)
        SetScaleX(1250)
        SetScaleY(1500)
        RandAddScaleY(500, 2000)
        RandAddScaleX(0, 500)
        SetZVal(-500)
        AddY(250000)
        AddX(300000)
    sprite('vr_mvef403a_00', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_01', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_02', 2)
    sprite('vr_mvef403a_03', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_00', 2)
    sprite('vr_mvef403a_01', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_02', 2)
    sprite('vr_mvef403a_03', 2)


@State
def mv403Smoke():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_cmnsmoke00', '')
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        AddX(150000)
        AlphaValue(126)
        SetScaleX(600)
        SetScaleY(400)
        physicsXImpulse(-7500)
    sprite('null', 10)
    sprite('null', 12)
    ConstantAlphaModifier(-8)


@State
def SuperHealEff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Eff3DEffect('ceef_superhealeff00.DIG', '')
        IgnoreScreenfreeze(1)
        AddY(500000)
        AddX(40000)
        BlendMode_Normal()
        uponSendToLabel(32, 1)
    sprite('null', 10)
    CreateObject('ceCmnHealAura', -1)

    def RunOnObject_1():
        AddScale(500)
    CreateParticle('ceef_healsphere_start', 100)
    CreateObject('SuperHealEff2', -1)
    CreateObject('SuperHealEff3', -1)
    Size(100)
    SetScaleSpeed(100)
    PrivateSE('cese_03')
    label(0)
    sprite('null', 1)
    CreateObject('ceCmnHealAura', -1)

    def RunOnObject_1():
        AddScale(500)
        AddX(70000)
    SetScaleSpeed(0)
    Size(1450)
    sprite('null', 3)
    RandAddScale(-100, 100)
    sprite('null', 1)
    SetScaleSpeed(0)
    Size(1450)
    sprite('null', 3)
    RandAddScale(-100, 100)
    sprite('null', 1)
    SetScaleSpeed(0)
    Size(1450)
    sprite('null', 3)
    RandAddScale(-100, 100)
    sprite('null', 1)
    SetScaleSpeed(0)
    Size(1450)
    sprite('null', 3)
    RandAddScale(-100, 100)
    sprite('null', 1)
    SetScaleSpeed(0)
    Size(1450)
    sprite('null', 3)
    RandAddScale(-100, 100)
    sprite('null', 1)
    SetScaleSpeed(0)
    Size(1450)
    sprite('null', 3)
    RandAddScale(-100, 100)
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    TriggerUponForState('SuperHealEff2', 32)
    TriggerUponForState('SuperHealEff3', 32)
    ConstantAlphaModifier(-26)
    SetScaleSpeed(30)
    sprite('null', 5)
    loopRest()


@State
def SuperHealEff3():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        LinkParticle('ceef_healaura00')
        IgnoreScreenfreeze(1)
        uponSendToLabel(32, 0)
        Size(800)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    CreateParticle('ceef_healauraend2', -1)
    ConstantAlphaModifier(-26)


@State
def SuperHealEffWing():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        BlendMode_Add()
        SetScaleX(1300)
        SetScaleY(1600)
        AddY(-150000)
        AddRotationPerFrame(-125)
        SetZVal(100)
        AlphaValue(200)
    sprite('vr_ce432b_00', 6)
    CreateObject('SuperHealEffWingL', -1)
    CreateParticle('ceef_odhealkira02', 0)
    sprite('vr_ce432b_01', 6)
    CreateParticle('ceef_odhealkira02', 0)
    sprite('vr_ce432b_02', 6)
    CreateParticle('ceef_odhealkira02', 0)
    sprite('vr_ce432b_03', 6)
    CreateParticle('ceef_odhealkira02', 0)
    SetScaleSpeed(5)
    sprite('vr_ce432b_04', 6)
    CreateParticle('ceef_odhealkira02', 0)
    sprite('vr_ce432b_05', 7)
    CreateParticle('ceef_odhealkira02', 0)
    sprite('vr_ce432b_06', 7)
    CreateParticle('ceef_odhealkira02', 0)
    sprite('vr_ce432b_07', 4)
    CreateParticle('ceef_odhealkira02', 0)
    sprite('vr_ce432b_08', 4)


@State
def SuperHealEffWingL():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        BlendMode_Add()
        Flip()
        SetScaleX(1400)
        SetScaleY(1600)
        AddRotationPerFrame(-125)
        SetZVal(100)
        AlphaValue(200)
    sprite('vr_ce432b_00', 6)
    CreateParticle('ceef_odhealkira02', 0)
    sprite('vr_ce432b_01', 6)
    CreateParticle('ceef_odhealkira02', 0)
    sprite('vr_ce432b_02', 6)
    CreateParticle('ceef_odhealkira02', 0)
    sprite('vr_ce432b_03', 6)
    CreateParticle('ceef_odhealkira02', 0)
    SetScaleSpeed(5)
    sprite('vr_ce432b_04', 6)
    CreateParticle('ceef_odhealkira02', 0)
    sprite('vr_ce432b_05', 7)
    CreateParticle('ceef_odhealkira02', 0)
    sprite('vr_ce432b_06', 7)
    CreateParticle('ceef_odhealkira02', 0)
    sprite('vr_ce432b_07', 4)
    CreateParticle('ceef_odhealkira02', 0)
    sprite('vr_ce432b_08', 4)


@State
def SuperHealEff2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Eff3DEffect('ceef_superhealeff01.DIG', '')
        IgnoreScreenfreeze(1)
        Size(1300)
        AddX(90000)
        uponSendToLabel(32, 1)
    sprite('null', 20)
    AlphaValue(0)
    ConstantAlphaModifier(17)
    sprite('null', 32767)
    LinkParticle('ceef_superheal01')
    label(1)
    sprite('null', 20)
    ConstantAlphaModifier(-17)
    loopRest()


@State
def SuperHealEffOD():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Eff3DEffect('ceef_superhealeff00.DIG', '')
        IgnoreScreenfreeze(1)
        AddY(500000)
        AddX(40000)
        BlendMode_Normal()
        uponSendToLabel(32, 1)
    sprite('null', 10)
    CreateObject('SuperHealEffWing', -1)
    CreateParticle('ceef_healsphere_start', 100)
    CreateObject('SuperHealEff2', -1)
    CreateObject('SuperHealEff3OD', -1)
    Size(200)
    SetScaleSpeed(100)
    PrivateSE('cese_03')
    label(0)
    sprite('null', 1)
    CreateObject('ceCmnHealAura', -1)

    def RunOnObject_1():
        AddScale(500)
        AddX(70000)
    SetScaleSpeed(0)
    Size(1450)
    sprite('null', 3)
    RandAddScale(-100, 100)
    sprite('null', 1)
    SetScaleSpeed(0)
    Size(1450)
    sprite('null', 3)
    RandAddScale(-100, 100)
    sprite('null', 1)
    SetScaleSpeed(0)
    Size(1450)
    sprite('null', 3)
    RandAddScale(-100, 100)
    sprite('null', 1)
    SetScaleSpeed(0)
    Size(1450)
    sprite('null', 3)
    RandAddScale(-100, 100)
    sprite('null', 1)
    SetScaleSpeed(0)
    Size(1450)
    sprite('null', 3)
    RandAddScale(-100, 100)
    sprite('null', 1)
    SetScaleSpeed(0)
    Size(1450)
    sprite('null', 3)
    RandAddScale(-100, 100)
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    TriggerUponForState('SuperHealEff2', 32)
    TriggerUponForState('SuperHealEff3OD', 32)
    ConstantAlphaModifier(-26)
    SetScaleSpeed(30)
    sprite('null', 5)
    loopRest()


@State
def SuperHealEff3OD():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        LinkParticle('ceef_healaura00od')
        IgnoreScreenfreeze(1)
        Size(1250)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    CreateParticle('ceef_healauraend2', -1)
    ConstantAlphaModifier(-26)


@State
def ceef_healjunbieff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        LinkParticle('ceef_healjunbieff')
        IgnoreScreenfreeze(1)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    CreateParticle('ceef_healtameendeff', -1)
    ConstantAlphaModifier(-17)


@State
def ceef_HealKurukuru():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
    sprite('vr_ce432_00', 6)
    AddX(-10000)
    sprite('vr_ce432_01', 6)
    AddX(10000)
    CreateParticle('ceef_kurukurutubu', 0)
    CreateParticle('ceef_kurukurutubu', 1)
    CreateParticle('ceef_kurukurutubu', 2)
    sprite('vr_ce432_02', 6)
    CreateParticle('ceef_kurukurutubu', 0)
    CreateParticle('ceef_kurukurutubu', 1)
    CreateParticle('ceef_kurukurutubu', 2)
    sprite('vr_ce432_03', 6)
    CreateParticle('ceef_kurukurutubu', 0)
    CreateParticle('ceef_kurukurutubu', 1)
    CreateParticle('ceef_kurukurutubu', 2)
    sprite('vr_ce432_04', 6)
    CreateParticle('ceef_kurukurutubu', 0)
    CreateParticle('ceef_kurukurutubu', 1)
    CreateParticle('ceef_kurukurutubu', 2)
    sprite('vr_ce432_05', 6)
    CreateParticle('ceef_kurukurutubu', 0)
    CreateParticle('ceef_kurukurutubu', 1)
    CreateParticle('ceef_kurukurutubu', 2)
    sprite('vr_ce432_06', 6)
    CreateParticle('ceef_kurukurutubu', 0)
    CreateParticle('ceef_kurukurutubu', 1)
    CreateParticle('ceef_kurukurutubu', 2)
    sprite('vr_ce432_07', 6)


@State
def ceef_HealJunbiAnim_R():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        Size(1200)
        RandAddScaleY(0, 450)
        DeviationX(-150000, 0)
        SetZVal(100)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(2)
        AfterimageColor_1(128, 0, 0, 0)
    sprite('vr_ce432a_00', 5)
    ConstantAlphaModifier(-4)
    PrivateSE('cese_02')
    sprite('vr_ce432a_01', 5)
    sprite('vr_ce432a_02', 5)
    sprite('vr_ce432a_03', 5)
    sprite('vr_ce432a_04', 5)
    sprite('vr_ce432a_05', 4)
    sprite('vr_ce432a_06', 4)
    sprite('vr_ce432a_07', 3)
    sprite('vr_ce432a_08', 3)


@State
def ceef_HealJunbiAnim_L():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        Size(1200)
        RandAddScaleY(0, 450)
        DeviationX(0, 150000)
        SetZVal(100)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(3)
    sprite('vr_ce432a_00', 5)
    ConstantAlphaModifier(-4)
    sprite('vr_ce432a_01', 5)
    sprite('vr_ce432a_02', 5)
    sprite('vr_ce432a_03', 5)
    sprite('vr_ce432a_04', 5)
    sprite('vr_ce432a_05', 4)
    sprite('vr_ce432a_06', 4)
    sprite('vr_ce432a_07', 3)
    sprite('vr_ce432a_08', 3)


@State
def ShungokuEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        TeleportToObject(22)
        AddY(280000)
        Eff3DEffect('ceef_shungokueff_bg.DIG', '')
        RenderLayer(2)
    sprite('null', 5)
    AlphaValue(0)
    ConstantAlphaModifier(51)
    CreateObject('ShungokuEff3', -1)
    CreateObject('ShungokuShake', -1)
    sprite('null', 30)
    LinkParticle('ceef_shungoku_b')
    CreateObject('ShungokuEff2', -1)
    sprite('null', 20)
    CreateObject('ShungokuEff4', -1)
    sprite('null', 5)
    PrivateSE('cese_13')


@State
def ShungokuEff2():

    def upon_IMMEDIATE():
        BlendMode_Add()
        Eff3DEffect('ceef_shungokueff00.DIG', '')
        IgnoreScreenfreeze(1)
        Size(990)
    sprite('null', 35)
    PrivateSE('cese_13')


@State
def ShungokuEff4():

    def upon_IMMEDIATE():
        BlendMode_Add()
        Eff3DEffect('ceef_shungokueff00.DIG', '')
        IgnoreScreenfreeze(1)
        Size(990)
        Rotation(-22500)
    sprite('null', 20)
    PrivateSE('cese_13')
    sprite('null', 15)
    Rotation(-60000)
    SetScaleY(2000)
    SetScaleX(600)
    ScreenShake(40000, 40000)
    PrivateSE('cese_13')


@State
def ShungokuShake():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
    label(0)
    sprite('null', 10)
    ScreenShake(10000, 10000)
    gotoLabel(0)


@State
def ShungokuEff3():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ceef_shungokueff01.DIG', '')
        IgnoreScreenfreeze(1)
        AddY(-100000)
        Size(900)
        AddY(28000)
    sprite('null', 4)
    PrivateSE('cese_13')
    sprite('null', 6)
    Size(1250)
    AddY(30000)
    PrivateSE('cese_13')
    sprite('null', 4)
    Size(1350)
    PrivateSE('cese_13')


@State
def HensinThunder():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        Eff3DEffect('ceef_shungokustart00.DIG', '')
        IgnoreScreenfreeze(1)
        Size(1250)
        AddX(-60000)
        SetScaleXPerFrame(10)
    sprite('null', 1)
    CreateObject('HensinThunderSub', -1)
    label(0)
    sprite('null', 4)
    AlphaValue(255)
    CommonSE('014_electric_m')
    sprite('null', 1)
    AlphaValue(0)
    gotoLabel(0)


@State
def HensinThunderSub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        LinkParticle('ceef_shungokutame00')
        Size(1500)
        IgnoreScreenfreeze(1)
    sprite('null', 32767)


@State
def ShungokuODSlashEff():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(2)
        Eff3DEffect('ceef_shungokuODeff00.DIG', '')
        IgnoreScreenfreeze(1)
        Size(1300)
        AddY(150000)
        Rotation(-20000)
        Flip()
        RenderLayer(2)
    sprite('null', 7)
    ParticleRotationAngle(-20000)
    CallCustomizableParticle('ceef_odshungokuspeed', -1)
    ScreenShake(20000, 20000)
    PrivateSE('cese_13')
    sprite('null', 6)
    ScreenShake(20000, 20000)


@State
def ShungokuODSlashEff2():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(2)
        Eff3DEffect('ceef_shungokuODeff00.DIG', '')
        IgnoreScreenfreeze(1)
        Size(1500)
        Rotation(-20000)
        AddY(150000)
        AddX(-100000)
        Flip()
        RenderLayer(2)
    sprite('null', 7)
    ParticleRotationAngle(-20000)
    CallCustomizableParticle('ceef_odshungokuspeed', -1)
    SetScaleXPerFrame(100)
    ScreenShake(20000, 20000)
    PrivateSE('cese_13')
    sprite('null', 6)
    ScreenShake(20000, 20000)


@State
def ShungokuODSlashEff3():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(2)
        Eff3DEffect('ceef_shungokuODeff00.DIG', '')
        IgnoreScreenfreeze(1)
        SetScaleY(2000)
        TeleportToObject(22)
        AddY(200000)
        RenderLayer(2)
        Flip()
    sprite('null', 7)
    CallCustomizableParticle('ceef_odshungokuspeed', -1)
    SetScaleXPerFrame(100)
    physicsXImpulse(-30000)
    ScreenShake(20000, 20000)
    PrivateSE('cese_13')
    sprite('null', 6)
    ScreenShake(20000, 20000)


@State
def ShungokuODFinishEff():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        AddY(150000)
    sprite('null', 18)
    sprite('null', 44)
    LinkParticle('ceef_shungokuodeff00')
    sprite('null', 1)
    CreateParticle('ceef_shungokuodeff_end', -1)
    ScreenShake(20000, 20000)


@State
def mv430ConsentEff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('ceef_205_plugeff_bigc')
        IgnoreScreenfreeze(1)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    CreateParticle('ceef_plugeff_cmnthunder', -1)
    ConstantAlphaModifier(-26)
    SetScaleSpeed(30)


@State
def ce440Eff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ceef_440ranbu00', '')
        Size(2000)
        IgnoreFinishStop(1)
    sprite('null', 4)
    sprite('null', 25)
    IgnoreFinishStop(0)
    ScreenShake(20000, 20000)


@State
def ce440Eff2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ceef_440ranbu01', '')
        Size(1500)
        AddX(200000)
        AddY(-100000)
        IgnoreFinishStop(1)
    sprite('null', 4)
    sprite('null', 15)
    IgnoreFinishStop(0)
    ScreenShake(20000, 20000)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def ce440Eff3():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ceef_440ranbu02', '')
        SetScaleX(1160)
        SetScaleY(1760)
        AddX(200000)
        AddY(-400000)
        IgnoreFinishStop(1)
    sprite('null', 4)
    sprite('null', 15)
    IgnoreFinishStop(0)
    ScreenShake(30000, 30000)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def ce440EffMato():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        AddX(600000)
        AddY(250000)
    label(0)
    sprite('null', 3)
    CreateObject('ce440EffCircle', -1)
    CreateObject('ce440EffCircle2', -1)

    def RunOnObject_1():
        AddScale(-200)
    gotoLabel(0)


@State
def ce440EffCircle():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ceef_440circle', '')
    sprite('null', 7)
    physicsXImpulse(-17500)
    sprite('null', 10)
    physicsXImpulse(-8750)
    SetScaleSpeed(120)
    ConstantAlphaModifier(-26)


@State
def ce440EffCircle2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('ceef_440circle', '')
    sprite('null', 7)
    physicsXImpulse(-35000)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def mv440Eff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('ceef_213eff00', '')
        BlendMode_Normal()
        SetScaleY(840)
        SetScaleX(480)
        AlphaValue(200)
        RotationAngle(-90000)
        AddY(200000)
        AddX(525000)
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 1)
    CreateObject('mv440EffSub', -1)
    CreateParticle('ceef440_cmnHit01', -1)
    AddScale(200)
    sprite('null', 1)
    AddScale(-200)
    sprite('null', 1)
    AddScale(200)
    sprite('null', 1)
    AddScale(-200)
    gotoLabel(0)
    label(1)
    sprite('null', 3)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def mv440EffSub():

    def upon_IMMEDIATE():
        AddY(-210000)
        AddX(-100000)
    sprite('null', 30)
    SetScaleSpeed(120)
    physicsXImpulse(-30000)
    LinkParticle('ceef_233shock00')


@State
def ceef_hiteff440():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        Rotation(35000)
        Size(1200)
        RandAddScaleX(200, 800)
        RandAddRotation(15000, 45000)
        RenderLayer(11)
        AlphaValue(255)
        AddX(75000)
        BlendMode_Add()
    sprite('vr_mvcmneff_00', 2)
    CreateObject('ceef_hiteff440sub', -1)
    sprite('vr_mvcmneff_01', 2)
    ConstantAlphaModifier(-8)
    sprite('vr_mvcmneff_02', 2)
    sprite('vr_mvcmneff_03', 2)
    sprite('vr_mvcmneff_04', 2)
    sprite('vr_mvcmneff_05', 2)
    sprite('vr_mvcmneff_07', 2)
    sprite('vr_mvcmneff_08', 2)


@State
def ceef_hiteff440sub():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        Rotation(35000)
        Size(1200)
        RandAddScaleX(200, 800)
        RandAddRotation(-45000, -15000)
        RenderLayer(11)
        AlphaValue(255)
        BlendMode_Add()
    sprite('vr_mvcmneff_00', 2)
    sprite('vr_mvcmneff_01', 2)
    ConstantAlphaModifier(-8)
    sprite('vr_mvcmneff_02', 2)
    sprite('vr_mvcmneff_03', 2)
    sprite('vr_mvcmneff_04', 2)
    sprite('vr_mvcmneff_05', 2)
    sprite('vr_mvcmneff_07', 2)
    sprite('vr_mvcmneff_08', 2)


@State
def ceef_hiteff440End():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        Size(2500)
        RenderLayer(11)
        AddX(-500000)
        BlendMode_Add()
    sprite('vr_mvcmneff3_00', 3)
    SetScaleSpeedY(-30)
    SetScaleXPerFrame(30)
    sprite('vr_mvcmneff3_01', 3)
    sprite('vr_mvcmneff3_02', 3)
    sprite('vr_mvcmneff3_03', 3)
    sprite('vr_mvcmneff3_04', 3)
    sprite('vr_mvcmneff3_05', 3)
    sprite('vr_mvcmneff3_06', 3)
    ConstantAlphaModifier(-26)
    sprite('vr_mvcmneff3_07', 3)
    sprite('vr_mvcmneff3_08', 3)


@State
def ceef_hiteff440HitEx():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Flip()
        Size(1500)
        Eff3DEffect('ceef_440hit00', '')
        BlendMode_Add()
        AddX(-400000)
        AddY(280000)
    sprite('null', 5)
    CreateParticle('ceef_tamebeam_end2', -1)
    sprite('null', 5)
    SetScaleSpeed(200)
    ConstantAlphaModifier(-51)


@State
def BurstDD_Camera():

    def upon_IMMEDIATE():
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        CameraNoCeiling(1)
        AddX(200000)
    sprite('null', 32767)


@State
def ceef450_Kousoku():

    def upon_IMMEDIATE():
        LinkParticle('ceef_healbaind_00')
        AddX(200000)
        WallCollisionDetection(1)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)

        def upon_EVERY_FRAME():
            if SLOT_2:
                TeleportToObject(22)
            else:
                PrivateFunction3(3, 200000, 0, 100, 0)
    sprite('null', 30)
    gotoLabel(1)
    label(0)
    sprite('null', 32767)
    SetActionMark(1)
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    CreateParticle('ceef_healbaind_end', -1)


@State
def ceef450_BG():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        Eff3DEffect('ceef_450_BG00', '')
        BlendMode_Normal()
        AddY(37500)
        uponSendToLabel(32, 0)
        RenderLayer(2)
        LinkParticle('ceef_healBG')
    sprite('null', 32767)
    CreateParticle('ceef_450_healaura_pos', -1)
    CreateObject('ceef450_BGa', -1)
    label(0)
    sprite('null', 30)
    TriggerUponForState('ceef450_BGa', 32)


@State
def ceef450_BGa():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        Eff3DEffect('ceef_450_BG00_a', '')
        BlendMode_Normal()
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    LinkParticle('ceef_450_healaura_kira')
    label(0)
    sprite('null', 10)
    CreateObject('ceef450_Ryuhai', -1)


@State
def ceef450_Ryuhai():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        Eff3DEffect('ceef_450_shasha', '')
        BlendMode_Normal()
        RenderLayer(1)
    sprite('null', 39)


@State
def AHCamera():

    def upon_IMMEDIATE():
        CameraControlEnable(1)
        CameraNoScreenCollision(1)
        CameraNoCeiling(1)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
    sprite('null', 180)
    physicsYImpulse(150000)
    sprite('null', 2)
    physicsYImpulse(10000)
    sprite('null', 2)
    physicsYImpulse(5000)
    sprite('null', 2)
    physicsYImpulse(0)
    sprite('null', 32767)
    CameraFast(1)
    label(0)
    sprite('null', 32767)
    TeleportToObject(22)
    CameraFast(1)
    label(1)
    sprite('null', 32767)
    TeleportToObject(3)


@State
def AHKiraEff():

    def upon_IMMEDIATE():
        CameraNoScreenCollision(1)
        CameraNoCeiling(1)
        AlphaValue(0)
        Size(450)
        Flip()
        AddX(400000)
        BlendMode_Normal()
    sprite('null', 20)
    LinkParticle('ceef_450ef_c')
    physicsYImpulse(62500)
    CreateObject('ceef450Shake', -1)
    PrivateSE('cese_24')
    sprite('null', 15)
    ConstantAlphaModifier(17)
    physicsYImpulse(187500)
    sprite('null', 153)
    physicsYImpulse(148000)
    sprite('null', 1)
    physicsYImpulse(0)
    AlphaValue(0)
    CreateObject('AHKiraEff2', -1)


@State
def AHKiraEff2():

    def upon_IMMEDIATE():
        CameraNoScreenCollision(1)
        CameraNoCeiling(1)
        SetScaleY(1100)
        SetScaleX(950)
    sprite('null', 35)
    Eff3DEffect('ceef_450line00', '')
    PrivateSE('cese_25')
    sprite('null', 1)
    physicsYImpulse(0)
    CreateObject('AHce450', -1)


@State
def AHce450():

    def upon_IMMEDIATE():
        CameraNoScreenCollision(1)
        CameraNoCeiling(1)
        SetScaleX(1000)
        Flip()
        AddX(350000)
        AddY(280000)
    sprite('ce450cutin_00', 60)
    LinkParticle('ceef_450cutinline01')
    CreateObject('ceef450Shake', -1)
    SetScaleSpeed(2)
    physicsYImpulse(225)
    physicsXImpulse(-750)
    PrivateSE('cese_26')
    sprite('ce450cutin_00', 10)
    ConstantAlphaModifier(-26)


@State
def ceef450Shake():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
    label(0)
    sprite('null', 8)
    ScreenShake(6000, 6000)
    gotoLabel(0)


@State
def ceef450_BG3():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_450_BG01', '')
        BlendMode_Normal()
        uponSendToLabel(32, 0)
    sprite('null', 75)
    AddX(400000)
    CreateObject('ceef450_BG3Eff', -1)
    sprite('null', 32767)
    Eff3DEffect('ceef_450_BG02', '')
    DespawnEAEffect('ceef450_BG3Eff')
    label(0)
    sprite('null', 20)
    TeleportToObject(3)
    TriggerUponForState('mv450WhiteOut', 32)
    LinkParticle('ceef_450_hanatiri')
    sprite('null', 32767)
    CreateObject('ceef_WinBG', -1)


@State
def ceef450_BG3Eff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
    sprite('null', 32767)
    LinkParticle('ceef_healBG')


@State
def ceef_WinBG():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        Eff3DEffect('ceef_450sky00', '')
    sprite('null', 32767)
    LinkParticle('ceef_450winbg')


@State
def mv450Smoke():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_cmnsmoke00', '')
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        AddX(10000)
        AlphaValue(255)
        SetScaleX(1200)
    sprite('null', 10)
    sprite('null', 12)
    ConstantAlphaModifier(-17)


@State
def mv450SmokeMato():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
    sprite('null', 4)
    CreateObject('mv450Smoke1', -1)
    ScreenShake(30000, 30000)
    PrivateSE('cese_14')
    PrivateSE('cese_14')
    sprite('null', 4)
    CreateObject('mv450Smoke1', -1)

    def RunOnObject_1():
        AddX(600000)
    sprite('null', 4)
    CreateObject('mv450Smoke1', -1)

    def RunOnObject_1():
        AddX(1200000)
        AddScaleY(-300)
    sprite('null', 6)
    CreateObject('mv450Smoke2', -1)


@State
def mv450Smoke1():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_cmnsmoke00', '')
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        AddX(20000)
        AlphaValue(255)
        SetScaleX(-1200)
        SetScaleY(1200)
    sprite('null', 10)
    sprite('null', 12)
    ConstantAlphaModifier(-17)


@State
def mv450Smoke2():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_450smoke00', '')
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        AddX(-200000)
        AlphaValue(0)
        SetScaleX(-1400)
    sprite('null', 10)
    ConstantAlphaModifier(26)
    sprite('null', 30)
    sprite('null', 60)
    ConstantAlphaModifier(-5)


@State
def mv450HanaTiri():

    def upon_IMMEDIATE():
        AddY(300000)
    sprite('null', 60)
    LinkParticle('ceef_450_hanatiri')
    sprite('null', 60)
    ConstantAlphaModifier(-5)


@State
def mv450WhiteOut():

    def upon_IMMEDIATE():
        AddY(300000)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 0)
        Size(2000)
    sprite('null', 60)
    sprite('null', 32767)
    LinkParticle('ceef_450_white')
    label(0)
    sprite('null', 10)
    AddY(300000)
    sprite('null', 60)
    ConstantAlphaModifier(-5)


@State
def ce450JetEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
        Flip()
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        LinkParticle('ceef_400_shock')
        Eff3DEffect('ceef_400eff00.DIG', '')
        Size(550)
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 5)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    loopRest()


@State
def mv450BomEff():

    def upon_IMMEDIATE():
        Eff3DEffect('ceeff_cmnbomb00', '')
        BlendMode_Normal()
        TeleportToObject(22)
        AddY(300000)
        AddX(150000)
        SetScaleY(1000)
        SetScaleX(800)
        Rotation(20000)
        IgnoreScreenfreeze(1)
        RenderLayer(1)
    sprite('null', 3)
    sprite('null', 3)
    CreateParticle('ceef_321_fallfireball00', -1)
    CreateParticle('ceef_321_fallfireball01', -1)
    CreateParticle('ceef_321_fallfireball02', -1)
    AddScale(250)
    sprite('null', 3)
    AddScale(150)
    CreateParticle('ceef_321_bloom', -1)
    ScreenShake(15000, 15000)
    sprite('null', 9)
    AddScale(100)


@State
def RecoveryCapa():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)

        def upon_EVERY_FRAME():
            EffectPosition(3, 103)
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
    sprite('null', 10)
    CreateObject('RecoveryCapa_buff', 100)
    CreateObject('RecoveryCapa_aura', 100)
    sprite('null', 10)
    CreateObject('RecoveryCapa_aura', 100)
    sprite('null', 10)
    CreateObject('RecoveryCapa_aura', 100)


@State
def RecoveryCapa_buff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        LinkParticle('ceef_RecoveryCapa_buff')
    sprite('null', 60)


@State
def RecoveryCapa_aura():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        LinkParticle('ceef_RecoveryCapa_aura')
    sprite('null', 15)
    sprite('null', 15)
    E0EAEffectPosition(0)


@State
def ce615Eff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        LinkParticle('ceef_enshutuheal')
    sprite('null', 10)
    label(0)
    sprite('null', 58)
    CreateObject('ceCmnHealAura', -1)
    gotoLabel(0)


@State
def ceCmnHealAura():

    def upon_IMMEDIATE():
        Eff3DEffect('ceef_cmnhealaura00', '')
        RandAddRotation(-15000, 10000)
        BlendMode_Normal()
        Size(650)
        IgnoreScreenfreeze(1)
    sprite('null', 58)
    ConstantAlphaModifier(-3)
    SetScaleSpeed(10)
    physicsYImpulse(500)


@State
def ce615Eff2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        LinkParticle('ceef_enemyhealaura')
        TeleportToObject(22)
    sprite('null', 32767)


@State
def Act2Event_Yure():
    label(0)
    sprite('null', 10)
    ScreenShake(3000, 3000)
    CommonSE('019_quake_0')
    loopRest()
    gotoLabel(0)


@State
def Act3Event_CreateNO():

    def upon_IMMEDIATE():
        LoadSpritePalette(0)
        XPositionRelativeFacing(-400000)
        SetZVal(-100)
        uponSendToLabel(32, 1)
    sprite('no064_04', 32767)
    loopRest()
    label(1)
    sprite('no032_02', 4)
    Flip()
    physicsXImpulse(32000)
    sprite('no032_03', 4)
    sprite('no032_04', 4)
    DashEffects(100, 1, 1)
    sprite('no032_05', 4)
    sprite('no032_06', 4)
    sprite('no032_07', 4)
    sprite('no032_08', 4)
    DashEffects(100, 1, 1)
    sprite('no032_09', 4)


@State
def Act3Event_HealEff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        LinkParticle('ceef_enemyhealaura')
    sprite('null', 32767)
    PrivateSE('cese_03')
