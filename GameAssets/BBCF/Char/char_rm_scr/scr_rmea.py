@State
def EMB_NY():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_LD.DIG', 'ef_emb_LD_motion_000.mmot')
        RenderLayer(5)
        BlendMode_Add()
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4278190335, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 10)
    ColorTransition(4294967295, 10)
    sprite('null', 15)
    sprite('null', 15)
    ColorTransition(4286625023, 10)
    AlphaValue(150)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(200)


@State
def EMB_NY_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_LD.DIG', 'ef_emb_LD_motion_000.mmot')
        RenderLayer(5)
        BlendMode_Add()
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4294967295, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 10)
    ColorTransition(4278223103, 10)
    sprite('null', 15)
    sprite('null', 15)
    ColorTransition(4278223103, 10)
    AlphaValue(150)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(200)


@State
def EMB_NY_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emb_LD.DIG', 'ef_emb_LD_motion_000.mmot')
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
    sprite('null', 20)
    ColorTransition(4278223103, 10)
    AlphaValue(150)
    ConstantAlphaModifier(-10)
    SetScaleSpeed(100)


@State
def DIST_NY5D():

    def upon_EVERY_FRAME():
        ParticleTransparency(1)
        PlayerTransparency(20000)
        Unknown3059(-1000)
        E0EAEffectRotation(2)
    sprite('vrdist_ny00', 6)
    SetScaleX(800)
    SetScaleY(600)
    SetScaleXPerFrame(150)
    SetScaleSpeedY(100)
    sprite('vrdist_ny00', 10)
    SetScaleSpeedY(-100)


@State
def DIST_NY5DADD():

    def upon_EVERY_FRAME():
        ParticleTransparency(1)
        PlayerTransparency(20000)
        Unknown3059(-1000)
        RotationAngle(36000)
    sprite('vrdist_ny00', 6)
    SetScaleX(800)
    SetScaleY(600)
    SetScaleXPerFrame(150)
    SetScaleSpeedY(100)
    sprite('vrdist_ny00', 10)
    SetScaleSpeedY(-100)


@State
def DIST_TriSwd():

    def upon_EVERY_FRAME():
        ParticleTransparency(1)
        PlayerTransparency(20000)
        Unknown3059(-1000)
    sprite('vrdist_ny00', 6)
    SetScaleX(1600)
    SetScaleY(1800)
    SetScaleXPerFrame(150)
    SetScaleSpeedY(150)
    sprite('vrdist_ny00', 10)
    SetScaleXPerFrame(-200)


@State
def NY_SummonA():
    PaletteIndex(1)
    sprite('null', 200)
    CreateObject('RM_SummonEff3d', -1)
    CreateParticle('rmef_sumA04', -1)
    ParticleColorFromPalette(229, 225, 229)
    CallCustomizableParticle('rmef_sumA', -1)
    if random_(2, 0, 33):
        PrivateSE('nyse_23')
    elif random_(2, 0, 50):
        PrivateSE('nyse_24')
    else:
        PrivateSE('nyse_25')


@State
def NY_SummonDmc():
    PaletteIndex(1)
    sprite('null', 200)
    CreateParticle('nyef_dmc00', -1)
    ParticleColorFromPalette(229, 226, 229)
    CallCustomizableParticle('rmef_dmc', -1)


@State
def NY_SummonAirDmc():
    PaletteIndex(1)
    sprite('null', 200)
    CreateParticle('nyef_airdmc00', -1)
    ParticleColorFromPalette(229, 226, 229)
    CallCustomizableParticle('rmef_airdmc', -1)


@State
def NY_SlowMc():
    PaletteIndex(1)
    sprite('null', 200)
    CreateParticle('nyef_slowmc01', -1)
    ParticleColorFromPalette(229, 225, 229)
    CallCustomizableParticle('nyef_slowmc', -1)


@State
def NY_SlowHand():
    PaletteIndex(1)
    sprite('null', 200)
    CreateParticle('nyef_slowhand01', -1)
    ParticleColorFromPalette(225, 225, 231)
    CallCustomizableParticle('nyef_slowhandcircle00', -1)
    ParticleColorFromPalette(225, 225, 226)
    CallCustomizableParticle('nyef_slowhand', -1)


@State
def NY_SumMultiSwordBigmc():
    PaletteIndex(1)
    sprite('null', 200)
    CreateParticle('nyef_sumDDstart00', -1)
    ParticleColorFromPalette(229, 225, 229)
    CallCustomizableParticle('nyef_sumDDstart01', -1)
    ParticleColorFromPalette(226, 226, 226)
    CallCustomizableParticle('nyef_sumDDstart02', -1)
    ParticleColorFromPalette(226, 225, 226)
    CallCustomizableParticle('rmef_sumDDstart03', -1)
    CallCustomizableParticle('nyef_sumDDstart', -1)


@State
def NY_SumMultiSwordBigmcOD():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 0)
        ParticleColorFromPalette(226, 225, 226)
        CallPrivateEffect('rmef_sumDDstart03b')
    sprite('null', 1000)
    CreateObject('NY_MultiSwordODSub', -1)
    CreateObject('NY_MultiSwordODSub2', -1)
    CreateObject('NY_MultiSwordODSub3', -1)
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    TriggerUponForState('NY_MultiSwordODSub', 32)
    TriggerUponForState('NY_MultiSwordODSub2', 32)
    TriggerUponForState('NY_MultiSwordODSub3', 32)


@State
def NY_MultiSwordODSub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    LinkParticle('rmef_sumDDstart00')
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def NY_MultiSwordODSub2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    ParticleColorFromPalette(229, 225, 229)
    CallPrivateEffect('nyef_sumDDstart01')
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def NY_MultiSwordODSub3():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    ParticleColorFromPalette(226, 226, 226)
    CallPrivateEffect('rmef_sumDDstart02')
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def NY_SumMultiSwordMc():
    PaletteIndex(1)
    sprite('null', 2)
    CreateParticle('nyef_sumDDlaser01', -1)
    ParticleColorFromPalette(225, 225, 226)
    CallCustomizableParticle('rmef_sumDDlaser', -1)


@State
def NY_SumBigSword():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        WallCollisionDetection(1)
    PaletteIndex(1)
    sprite('null', 200)
    CreateParticle('nyef_sumDD03', -1)
    ParticleSize(2000)
    ParticleColorFromPalette(229, 225, 229)
    CallCustomizableParticle('rmef_sumDD', -1)


@State
def NY_SlowFieldStart():
    PaletteIndex(1)
    sprite('null', 200)
    CreateParticle('nyef_slowfieldstart', -1)
    ParticleColorFromPalette(226, 227, 226)
    CallCustomizableParticle('nyef_slowmagic', -1)
    ParticleColorFromPalette(229, 230, 229)
    CallCustomizableParticle('nyef_slowmagicloop', -1)


@State
def NY_SlowField():
    PaletteIndex(1)
    sprite('null', 200)
    CreateParticle('nyef_slowlight', -1)
    CreateParticle('nyef_slowfieldloop', -1)
    ParticleColorFromPalette(229, 230, 229)
    CallCustomizableParticle('nyef_slowmagicloop', -1)


@State
def NY_ActP2_Down():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        AddX(32000)
        AddY(0)
        LinkParticle('nyef_act2_down')
        AlphaValue(255)
    sprite('null', 200)
    ConstantAlphaModifier(-5)


@State
def NY_ActP2_Up():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        AddX(104000)
        AddY(220000)
        LinkParticle('nyef_act2_up')
        AlphaValue(255)
    sprite('null', 200)
    ConstantAlphaModifier(-5)


@State
def NY_MagicA():
    sprite('null', 200)
    CreateParticle('nyef_mcircle', -1)


@State
def SummonSlowArea():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)

        def upon_32():
            AddX(300000)

        def upon_33():
            AddX(700000)

        def upon_34():
            AddX(1100000)

        def upon_35():
            CreateParticle('nyef_slowfieldend', -1)
            DeleteObject(23)
        RunLoopUpon(17, 180)

        def upon_17():
            sendToLabel(1)
    sprite('null', 1)
    sprite('null', 20)
    CreateObject('NY_SlowFieldStart', -1)
    PrivateSE('nyse_02')
    SlowField(1)
    label(0)
    sprite('null', 20)
    CreateObject('NY_SlowField', -1)
    CommonSE('022_magiccircle_c')
    sprite('null', 20)
    CreateObject('NY_SlowField', -1)
    sprite('null', 20)
    CreateObject('NY_SlowField', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 20)
    CreateParticle('nyef_slowfieldend', -1)


@Subroutine
def DriveSwordInit():
    AttackDefaults_Projectile()
    AttackLevel_(4)
    ProjectileLevel(2)
    Damage(600)
    AttackP1(80)
    UseSlashHitspark(1)
    HitsparkSize(600)
    StarterRating(2)
    EnemyHitstopAddition(0, 4, 9)
    Size(950)
    PaletteIndex(1)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(3)
    AfterimageSize_1(1000)
    AfterimageSize_2(1000)

    def upon_32():
        SetActionMark(1)
        AttackLevel_(5)
        Size(1150)
        SLOT_58 = 1

    def upon_OPPONENT_HIT_OR_BLOCK():
        CreateParticle('nyef_breakA', 101)
        CopyFromRightToLeft(3, 2, 59, 25, 2, 83)
        CopyFromRightToLeft(3, 2, 60, 25, 2, 23)
        if SLOT_58:
            ScreenShake(2000, 2000)

    def upon_EVERY_FRAME():
        if random_(2, 0, 50):
            clearUponHandler(EVERY_FRAME)
            ObjectUpon(LANDING, 41)
    uponSendToLabel(LANDING, 580)
    HitsPerCall(1, 0, 0, 1, 1, 0, 1, 1)
    uponSendToLabel(54, 580)


@Subroutine
def DriveSwordInit_Air():
    AttackDefaults_Projectile()
    AttackLevel_(4)
    ProjectileLevel(2)
    Damage(600)
    AttackP1(80)
    Hitstun(10)
    AirUntechableTime(10)
    UseSlashHitspark(1)
    HitsparkSize(600)
    StarterRating(2)
    CHGroundedHitstunAnimation(1)
    EnemyHitstopAddition(0, 4, 9)
    Size(950)
    PaletteIndex(1)
    EnableAfterimage(1)
    AfterimageBlendMode(2)
    AfterimageCount(3)
    AfterimageSize_1(1000)
    AfterimageSize_2(1000)

    def upon_32():
        SetActionMark(1)
        GroundedHitstunAnimation(1)
        AttackLevel_(5)
        Size(1150)
        SLOT_58 = 1

    def upon_OPPONENT_HIT_OR_BLOCK():
        CreateParticle('nyef_breakA', 101)
        CopyFromRightToLeft(3, 2, 59, 25, 2, 83)
        CopyFromRightToLeft(3, 2, 60, 25, 2, 23)
        if SLOT_58:
            ScreenShake(2000, 2000)

    def upon_EVERY_FRAME():
        if random_(2, 0, 50):
            clearUponHandler(EVERY_FRAME)
            ObjectUpon(LANDING, 41)
    uponSendToLabel(LANDING, 580)
    HitsPerCall(1, 0, 0, 1, 1, 0, 1, 1)
    uponSendToLabel(54, 580)


@Subroutine
def DriveSwordLandingParam():
    AttackOff()
    RotationSomething(0)
    EndMomentum(1)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    BlendMode_Normal()
    AlphaValue(250)
    ConstantAlphaModifier(-20)
    CreateObject('NY_MagicA', -1)
    CreateObject('DIST_NY5D', -1)


@Subroutine
def DriveSwordBreakParam():
    AttackOff()
    RotationSomething(0)
    EndMomentum(1)
    SetScaleXPerFrame(60)
    SetScaleSpeedY(-60)
    BlendMode_Normal()
    AlphaValue(250)
    ConstantAlphaModifier(-20)
    CreateObject('NY_MagicA', -1)
    CreateObject('DIST_NY5D', -1)


@State
def NY_Sword5D():

    def upon_IMMEDIATE():
        callSubroutine('DriveSwordInit')
        AddX(180000)
        AddY(180000)
        physicsXImpulse(25000)
        physicsYImpulse(0)
        AirPushbackY(16000)
        AirPushbackX(3000)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            TriggerUponForState('NmlAtk5D', 33)
    sprite('vrnyef_swda00', 2)
    CreateObject('NY_SummonA', 0)
    sprite('vrnyef_swda01', 2)
    sprite('vrnyef_swda02', 2)
    sprite('vrnyef_swda03', 2)
    sprite('vrnyef_swda04', 2)
    sprite('vrnyef_swda05', 2)
    sprite('vrnyef_swdaatk', 12)
    if not SLOT_2:
        ProjectileLevel(1)
    XImpulseAcceleration(157)
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')


@State
def NY_Sword5DEntryVsRg():

    def upon_IMMEDIATE():
        callSubroutine('DriveSwordInit')
        SetZVal(-500)

    def upon_EVERY_FRAME():
        if SLOT_19 < 260000:
            sendToLabel(580)
    sprite('vrnyef_swda00', 2)
    CreateObject('NY_SummonA', 0)
    sprite('vrnyef_swda01', 2)
    sprite('vrnyef_swda02', 2)
    sprite('vrnyef_swda03', 2)
    sprite('vrnyef_swda04', 2)
    sprite('vrnyef_swda05', 2)
    sprite('vrnyef_swdaatk', 120)
    RefreshMultihit()
    XImpulseAcceleration(315)
    loopRest()
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    loopRest()
    ExitState()
    label(580)
    clearUponHandler(EVERY_FRAME)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')
    ParticleColor(4278223103, 4278202623, 4278190335)
    if not SLOT_51:
        ParticleFacing(1)
    CallCustomizableParticle('ef_girdm', 0)
    ScreenShake(8000, 2000)
    CommonSE('105_guard_slash_2')
    ObjectUpon(LANDING, 33)
    loopRest()


@State
def NY_Sword6D():

    def upon_IMMEDIATE():
        callSubroutine('DriveSwordInit')
        AddX(150000)
        AddY(300000)
        physicsXImpulse(31200)
        physicsYImpulse(6300)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            TriggerUponForState('NmlAtk6D', 33)
    sprite('vrnyef_swdb00a', 2)
    CreateObject('NY_SummonA', 0)
    sprite('vrnyef_swdb01a', 2)
    sprite('vrnyef_swdb02a', 1)
    sprite('vrnyef_swdb03a', 1)
    sprite('vrnyef_swdb04a', 1)
    sprite('vrnyef_swdb05a', 1)
    sprite('vrnyef_swdb06a', 1)
    sprite('vrnyef_swdbaatk', 20)
    if not SLOT_2:
        ProjectileLevel(1)
    XImpulseAcceleration(210)
    YAccel(210)
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')


@State
def NY_Sword2D():

    def upon_IMMEDIATE():
        callSubroutine('DriveSwordInit')
        AddX(130000)
        AddY(330000)
        physicsXImpulse(33000)
        physicsYImpulse(26000)
        AirHitstunAnimation(13)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            TriggerUponForState('NmlAtk2D', 33)
    sprite('vrnyef_swdc00a', 1)
    CreateObject('NY_SummonA', 0)
    sprite('vrnyef_swdc01a', 1)
    sprite('vrnyef_swdc02a', 1)
    sprite('vrnyef_swdc03a', 1)
    sprite('vrnyef_swdc04a', 1)
    sprite('vrnyef_swdc05a', 1)
    sprite('vrnyef_swdc06a', 1)
    sprite('vrnyef_swdc07a', 1)
    sprite('vrnyef_swdc08a', 1)
    sprite('vrnyef_swdcatka', 20)
    if not SLOT_2:
        ProjectileLevel(1)
    XImpulseAcceleration(160)
    YAccel(160)
    SetScaleSpeed(25)
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')


@State
def NY_SwordAirD():

    def upon_IMMEDIATE():
        callSubroutine('DriveSwordInit_Air')
        AddX(192000)
        AddY(224000)
        physicsXImpulse(41400)
        physicsYImpulse(5760)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            TriggerUponForState('NmlAtkAIR5D', 33)
    sprite('vrnyef_swde00a', 1)
    CreateObject('NY_SummonA', 0)
    sprite('vrnyef_swde01a', 1)
    sprite('vrnyef_swde02a', 1)
    sprite('vrnyef_swde03a', 1)
    sprite('vrnyef_swde04a', 1)
    sprite('vrnyef_swde05a', 1)
    sprite('vrnyef_swde00aatk', 2)
    XImpulseAcceleration(180)
    YAccel(180)
    sprite('vrnyef_swde00aatk', 8)
    if not SLOT_2:
        ProjectileLevel(1)
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')


@State
def NY_SwordAir2D():

    def upon_IMMEDIATE():
        callSubroutine('DriveSwordInit_Air')
        AddX(192000)
        AddY(96000)
        physicsXImpulse(19200)
        physicsYImpulse(-12800)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            TriggerUponForState('NmlAtkAIR2D', 33)
    sprite('vrnyef_swde00c', 1)
    CreateObject('NY_SummonA', 0)
    sprite('vrnyef_swde01c', 1)
    sprite('vrnyef_swde02c', 1)
    sprite('vrnyef_swde03c', 1)
    sprite('vrnyef_swde04c', 1)
    sprite('vrnyef_swde05c', 1)
    sprite('vrnyef_swde00catk', 2)
    XImpulseAcceleration(160)
    YAccel(160)
    sprite('vrnyef_swde00catk', 6)
    if not SLOT_2:
        ProjectileLevel(1)
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')


@State
def NY_SwordAir6D():

    def upon_IMMEDIATE():
        callSubroutine('DriveSwordInit_Air')
        AddX(192000)
        AddY(144000)
        physicsXImpulse(36800)
        physicsYImpulse(-3200)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            TriggerUponForState('NmlAtkAIR6D', 33)
    sprite('vrnyef_swde00', 1)
    CreateObject('NY_SummonA', 0)
    sprite('vrnyef_swde01b', 1)
    sprite('vrnyef_swde02b', 1)
    sprite('vrnyef_swde03b', 1)
    sprite('vrnyef_swde04b', 1)
    sprite('vrnyef_swde05b', 1)
    sprite('vrnyef_swde00batk', 2)
    XImpulseAcceleration(160)
    YAccel(160)
    sprite('vrnyef_swde00batk', 4)
    if not SLOT_2:
        ProjectileLevel(1)
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')


@State
def NY_Sword4D():

    def upon_IMMEDIATE():
        callSubroutine('DriveSwordInit')
        if SLOT_19 > 600000:
            TeleportToObject(22)
            AddX(150000)
        else:
            AddX(650000)
            AddX(150000)
        AbsoluteY(580000)
        physicsXImpulse(-1666)
        physicsYImpulse(-4333)
        CreateObject('NY_SummonA', 0)
        AttackP1(70)
        BonusProration(110)
        PushbackX(-19800)
        GroundedHitstunAnimation(3)
        HitOverhead(2)

        def upon_OPPONENT_CHAR_HIT_OR_BLOCK():
            TriggerUponForState('NmlAtk4D', 33)
    sprite('vrnyef_swdd00a', 6)
    AttackOff()
    sprite('vrnyef_swdd01a', 3)
    sprite('vrnyef_swdd02a', 3)
    sprite('vrnyef_swdd03a', 3)
    sprite('vrnyef_swdd04a', 3)
    sprite('vrnyef_swdd05a', 3)
    sprite('vrnyef_swddaatk', 2)
    XImpulseAcceleration(1430)
    YAccel(1430)
    sprite('vrnyef_swddaatk', 3)
    RefreshMultihit()
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')


@State
def NY_SwordDChain():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(4)
        Damage(300)
        AttackP1(80)
        AirUntechableTime(25)
        Hitstun(22)
        Hitstop(5)
        HitsparkSize(600)
        UseSlashHitspark(1)
        StarterRating(2)
        CHStateIfCHStart(2)
        Size(900)
        PaletteIndex(1)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        CopyFromRightToLeft(23, 2, 83, 3, 2, 59)
        CopyFromRightToLeft(23, 2, 23, 3, 2, 60)
        CancelIfPlayerHit(3)

        def upon_OPPONENT_HIT_OR_BLOCK():
            CreateParticle('nyef_breakA', 101)
            clearUponHandler(OPPONENT_HIT_OR_BLOCK)
            ObjectUpon(LANDING, 32)
        uponSendToLabel(LANDING, 1)

        def upon_32():
            AirHitstunAnimation(10)
            PushbackX(19800)
            AirPushbackX(2000)
            AirPushbackY(20000)
            CHGroundedHitstunAnimation(2)
            CHStagger(58)
            CHCrumple(58)
            AddX(-200000)
            AddY(400000)
            physicsXImpulse(20000)
            physicsYImpulse(-9000)
            SetAcceleration(2000)
            setGravity(900)
            RotationSomething(0)
            CreateObject('NY_SummonA', -1)

        def upon_33():
            AirHitstunAnimation(18)
            PushbackX(12000)
            AirPushbackX(-8000)
            AirPushbackY(30000)
            AddX(160000)
            AddY(-100000)
            physicsXImpulse(-7000)
            physicsYImpulse(36000)
            SetAcceleration(-700)
            setGravity(-3600)
            RotationSomething(0)
            CreateObject('NY_SummonA', -1)

        def upon_34():
            AirHitstunAnimation(11)
            PushbackX(-19800)
            AirPushbackX(-12000)
            AirPushbackY(32000)
            AddX(300000)
            AddY(50000)
            physicsXImpulse(-20000)
            physicsYImpulse(10000)
            SetAcceleration(-2000)
            setGravity(-1000)
            RotationSomething(0)
            CreateObject('NY_SummonA', -1)

        def upon_35():
            AirPushbackY(0)
            AddX(-200000)
            AddY(400000)
            physicsXImpulse(12500)
            physicsYImpulse(-5000)
            SetAcceleration(2500)
            setGravity(1000)
            RotationSomething(0)
            CreateObject('NY_SummonA', -1)

        def upon_36():
            AirHitstunAnimation(10)
            PushbackX(-19800)
            AirPushbackX(-6000)
            AirPushbackY(8000)
            AddX(225000)
            AddY(540000)
            physicsXImpulse(-10000)
            physicsYImpulse(-26000)
            SetAcceleration(-1000)
            setGravity(2600)
            RotationSomething(0)
            CreateObject('NY_SummonA', -1)

        def upon_37():
            AirHitstunAnimation(10)
            AirPushbackX(2000)
            AirPushbackY(32000)
            AddX(-210000)
            AddY(0)
            physicsXImpulse(14000)
            physicsYImpulse(12000)
            SetAcceleration(1400)
            setGravity(-1200)
            RotationSomething(0)
            CreateObject('NY_SummonA', -1)

        def upon_38():
            AirHitstunAnimation(10)
            PushbackX(-19800)
            AirPushbackX(-12000)
            AddX(280000)
            AddY(0)
            physicsXImpulse(-18000)
            physicsYImpulse(22000)
            SetAcceleration(-1800)
            setGravity(-2200)
            RotationSomething(0)
            CreateObject('NY_SummonA', -1)
        HitsPerCall(1, 0, 0, 1, 1, 0, 1, 1)
        uponSendToLabel(54, 580)
    sprite('vrnyef_swdchain00', 1)
    AlphaValue(0)
    ConstantAlphaModifier(30)
    sprite('vrnyef_swdchain01', 1)
    sprite('vrnyef_swdchain02', 1)
    sprite('vrnyef_swdchain03', 1)
    sprite('vrnyef_swdchain04', 1)
    sprite('vrnyef_swdchain05', 1)
    sprite('vrnyef_swdchainatk', 10)
    XImpulseAcceleration(180)
    YAccel(180)
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')


@State
def NY_SwordDChainOD():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(5)
        Damage(600)
        AttackP1(80)
        Blockstun(22)
        AirUntechableTime(27)
        Hitstun(25)
        Hitstop(5)
        HitsparkSize(600)
        UseSlashHitspark(1)
        StarterRating(2)
        CHStateIfCHStart(2)
        Size(1100)
        PaletteIndex(1)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        CancelIfPlayerHit(3)

        def upon_OPPONENT_HIT_OR_BLOCK():
            ScreenShake(5000, 5000)
            CreateParticle('nyef_breakA', 101)
            ObjectUpon(LANDING, 32)
        uponSendToLabel(LANDING, 1)
        CopyFromRightToLeft(23, 2, 83, 3, 2, 59)
        CopyFromRightToLeft(23, 2, 23, 3, 2, 60)

        def upon_32():
            GroundedHitstunAnimation(2)
            AirHitstunAnimation(10)
            PushbackX(19800)
            AirPushbackX(2000)
            AirPushbackY(20000)
            AddX(-200000)
            AddY(400000)
            physicsXImpulse(20000)
            physicsYImpulse(-9000)
            SetAcceleration(2000)
            setGravity(900)
            RotationSomething(0)
            CreateObject('NY_SummonA', -1)

        def upon_33():
            AirHitstunAnimation(18)
            PushbackX(12000)
            AirPushbackX(-8000)
            AirPushbackY(30000)
            AddX(160000)
            AddY(-100000)
            physicsXImpulse(-7000)
            physicsYImpulse(36000)
            SetAcceleration(-700)
            setGravity(-3600)
            RotationSomething(0)
            CreateObject('NY_SummonA', -1)

        def upon_34():
            AirHitstunAnimation(11)
            PushbackX(-19800)
            AirPushbackX(-12000)
            AirPushbackY(32000)
            AddX(300000)
            AddY(50000)
            physicsXImpulse(-20000)
            physicsYImpulse(10000)
            SetAcceleration(-2000)
            setGravity(-1000)
            RotationSomething(0)
            CreateObject('NY_SummonA', -1)

        def upon_35():
            AirPushbackY(0)
            AddX(-200000)
            AddY(400000)
            physicsXImpulse(12500)
            physicsYImpulse(-5000)
            SetAcceleration(2500)
            setGravity(1000)
            RotationSomething(0)
            CreateObject('NY_SummonA', -1)

        def upon_36():
            AirHitstunAnimation(10)
            PushbackX(-19800)
            AirPushbackX(-6000)
            AirPushbackY(8000)
            AddX(225000)
            AddY(540000)
            physicsXImpulse(-10000)
            physicsYImpulse(-26000)
            SetAcceleration(-1000)
            setGravity(2600)
            RotationSomething(0)
            CreateObject('NY_SummonA', -1)

        def upon_37():
            AirHitstunAnimation(10)
            AirPushbackX(2000)
            AirPushbackY(32000)
            AddX(-210000)
            AddY(0)
            physicsXImpulse(14000)
            physicsYImpulse(12000)
            SetAcceleration(1400)
            setGravity(-1200)
            RotationSomething(0)
            CreateObject('NY_SummonA', -1)

        def upon_38():
            AirHitstunAnimation(10)
            PushbackX(-19800)
            AirPushbackX(-12000)
            AddX(280000)
            AddY(0)
            physicsXImpulse(-18000)
            physicsYImpulse(22000)
            SetAcceleration(-1800)
            setGravity(-2200)
            RotationSomething(0)
            CreateObject('NY_SummonA', -1)
        HitsPerCall(1, 0, 0, 1, 1, 0, 1, 1)
        uponSendToLabel(54, 580)
    sprite('vrnyef_swdchain00', 1)
    AlphaValue(0)
    ConstantAlphaModifier(30)
    sprite('vrnyef_swdchain01', 1)
    sprite('vrnyef_swdchain02', 1)
    sprite('vrnyef_swdchain03', 1)
    sprite('vrnyef_swdchain04', 1)
    sprite('vrnyef_swdchain05', 1)
    sprite('vrnyef_swdchainatk', 10)
    XImpulseAcceleration(180)
    YAccel(180)
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')


@State
def NY_BlackArea():

    def upon_IMMEDIATE():
        SetZVal(-500)
        AddX(160000)
    sprite('null', 120)
    CreateParticle('nyef_blackptcstart', -1)
    CreateParticle('nyef_sumlight00', -1)


@State
def NY_TripleSword11Mode():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        SLOT_51 = 27

        def upon_33():
            SLOT_51 = 200

        def upon_32():
            ObjectUpon(FALLING, 41)
            ObjectUpon(5, 41)
            ObjectUpon(6, 41)
            ObjectUpon(CORNERED, 41)
            ObjectUpon(8, 41)
            sendToLabel(1)

        def upon_PLAYER_DAMAGED():
            ObjectUpon(FALLING, 41)
            ObjectUpon(5, 41)
            ObjectUpon(6, 41)
            ObjectUpon(CORNERED, 41)
            ObjectUpon(8, 41)
            sendToLabel(1)

        def upon_EVERY_FRAME():
            if SLOT_51:
                SLOT_51 = SLOT_51 + -1
                if not SLOT_51:
                    sendToLabel(1)
            if SLOT_XDistanceFromCenterOfStage > 2100000:
                sendToLabel(1)
                clearUponHandler(EVERY_FRAME)
            if SLOT_XDistanceFromCenterOfStage < -2100000:
                sendToLabel(1)
                clearUponHandler(EVERY_FRAME)
        if CharacterIDCheck('ta'):
            clearUponHandler(EVERY_FRAME)

            def upon_EVERY_FRAME():
                if SLOT_51:
                    SLOT_51 = SLOT_51 + -1
                    if not SLOT_51:
                        sendToLabel(1)
                if SLOT_XDistanceFromCenterOfStage > 3900000:
                    sendToLabel(1)
                    clearUponHandler(EVERY_FRAME)
                if SLOT_XDistanceFromCenterOfStage < -3900000:
                    sendToLabel(1)
                    clearUponHandler(EVERY_FRAME)
        AddX(100000)
    sprite('null', 1)
    CreateObject('NY_BlackArea', -1)
    sprite('null', 1)
    CancelIfPlayerHit(0)
    label(0)
    sprite('null', 8)
    AddX(180000)
    CreateParticle('nyef_blackptcstart', -1)
    RegisterObject(8, 7)
    RegisterObject(7, 6)
    RegisterObject(6, 5)
    RegisterObject(5, 4)
    CreateObject('NY_SwordD400_Attack11Mode', -1)
    RegisterObject(4, 1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 10)


@State
def NY_TripleSword13Mode():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)
        SLOT_51 = 200

        def upon_32():
            ObjectUpon(FALLING, 41)
            ObjectUpon(5, 41)
            ObjectUpon(6, 41)
            ObjectUpon(CORNERED, 41)
            ObjectUpon(8, 41)
            sendToLabel(1)

        def upon_39():
            SLOT_51 = 27

        def upon_EVERY_FRAME():
            if SLOT_51:
                SLOT_51 = SLOT_51 + -1
                if not SLOT_51:
                    sendToLabel(1)
            if SLOT_XDistanceFromCenterOfStage > 2100000:
                sendToLabel(1)
                clearUponHandler(EVERY_FRAME)
            if SLOT_XDistanceFromCenterOfStage < -2100000:
                sendToLabel(1)
                clearUponHandler(EVERY_FRAME)
        if CharacterIDCheck('ta'):
            clearUponHandler(EVERY_FRAME)

            def upon_EVERY_FRAME():
                if SLOT_51:
                    SLOT_51 = SLOT_51 + -1
                    if not SLOT_51:
                        sendToLabel(1)
                if SLOT_XDistanceFromCenterOfStage > 3900000:
                    sendToLabel(1)
                    clearUponHandler(EVERY_FRAME)
                if SLOT_XDistanceFromCenterOfStage < -3900000:
                    sendToLabel(1)
                    clearUponHandler(EVERY_FRAME)
        AddX(70000)
    sprite('null', 1)
    CreateObject('NY_BlackArea', -1)
    sprite('null', 1)
    CancelIfPlayerHit(0)
    label(0)
    sprite('null', 8)
    AddX(180000)
    CreateParticle('nyef_blackptcstart', -1)
    RegisterObject(8, 7)
    RegisterObject(7, 6)
    RegisterObject(6, 5)
    RegisterObject(5, 4)
    CreateObject('NY_SwordD400_Attack13Mode', -1)
    RegisterObject(4, 1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 10)


@State
def NY_SwordD400_effA():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        BlendMode_Add()
        SetZVal(-100)
        AddX(-30000)
        RotationAngle(-65000)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageInterval(1)
        AfterimageCount(6)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
    sprite('null', 2)
    sprite('vrnyef_swd400a', 8)
    AlphaValue(80)
    ConstantAlphaModifier(20)
    physicsXImpulse(5000)
    physicsYImpulse(14000)
    sprite('vrnyef_swd400a', 12)
    ConstantAlphaModifier(-24)


@State
def NY_SwordD400_effB():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        BlendMode_Add()
        SetZVal(-100)
        AddX(60000)
        RotationAngle(245000)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageInterval(1)
        AfterimageCount(6)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
    sprite('null', 2)
    sprite('vrnyef_swd400a', 8)
    AlphaValue(80)
    ConstantAlphaModifier(20)
    physicsXImpulse(-5000)
    physicsYImpulse(15000)
    sprite('vrnyef_swd400a', 12)
    ConstantAlphaModifier(-20)


@State
def NY_SwordD400_Attack13Mode():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(4)
        AttackP2(80)
        SameMoveProration(10)
        UseSlashHitspark(1)
        EnemyHitstopAddition(15, 15, 15)

        def upon_OPPONENT_HIT_OR_BLOCK():
            ObjectUpon(LANDING, 32)
        E0EAEffectScale(2)
        Damage(1200)
        Hitstop(0)
        PushbackX(20000)
        AirPushbackY(38000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(40)

        def upon_41():
            EndAttack()
        PaletteIndex(1)
        RotationAngle(-90000)
        EnableAfterimage(1)
        AfterimageInterval(2)
        AfterimageCount(3)
        AfterimageColor_1(128, 255, 0, 0)
        AfterimageColor_2(255, 255, 0, 0)
        AfterimageSize_1(1050)
        AfterimageSize_2(1100)
    sprite('vrnyef_swd400atk00', 12)
    AlphaValue(240)
    setGravity(-800)
    SetScaleX(520)
    SetScaleXPerFrame(40)
    AddY(-104000)
    sprite('vrnyef_swd400atk01', 1)
    setGravity(-8000)
    AddY(42000)
    SetScaleSpeed(0)
    Size(1000)
    sprite('vrnyef_swd400atk02', 1)
    sprite('vrnyef_swd400atk03', 1)
    sprite('vrnyef_swd400atk', 6)
    setGravity(-6000)
    physicsYImpulse(24000)
    sprite('vrnyef_swd400atk', 10)
    setGravity(0)
    physicsYImpulse(16000)
    SetScaleXPerFrame(-10)
    SetScaleSpeedY(-100)
    AlphaValue(120)
    ConstantAlphaModifier(-12)
    EndAttack()
    CreateObject('NY_MagicA', -1)
    CreateObject('DIST_TriSwd', -1)
    CreateParticle('nyef_blackptcdel', -1)


@State
def NY_SwordD400_Attack11Mode():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(5)
        ProjectileLevel(2)
        Damage(1200)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        SingleProration(1)
        SameMoveProration(10)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(40)
        AirPushbackY(36000)
        AirPushbackX(3000)
        PushbackX(19800)
        Hitstop(0)
        EnemyHitstopAddition(15, 15, 15)
        UseSlashHitspark(1)
        VoodooDamageMultiplier(2)

        def upon_OPPONENT_HIT_OR_BLOCK():
            ObjectUpon(LANDING, 32)
        E0EAEffectScale(2)

        def upon_41():
            EndAttack()
        PaletteIndex(1)
        RotationAngle(-90000)
        EnableAfterimage(1)
        AfterimageInterval(2)
        AfterimageCount(3)
        AfterimageColor_1(200, 200, 200, 0)
        AfterimageColor_2(200, 200, 200, 0)
        AfterimageSize_1(1050)
        AfterimageSize_2(1100)
    sprite('vrnyef_swd400atk00', 12)
    AlphaValue(240)
    setGravity(-800)
    AddY(-104000)
    SetScaleX(520)
    SetScaleXPerFrame(40)
    PrivateSE('nyse_32')
    sprite('vrnyef_swd400atk01', 1)
    setGravity(-8000)
    AddY(42000)
    SetScaleSpeed(0)
    Size(1000)
    sprite('vrnyef_swd400atk02', 1)
    sprite('vrnyef_swd400atk03', 1)
    sprite('vrnyef_swd400atk', 6)
    setGravity(-6000)
    physicsYImpulse(24000)
    sprite('vrnyef_swd400atk', 10)
    setGravity(0)
    physicsYImpulse(16000)
    SetScaleXPerFrame(-10)
    SetScaleSpeedY(-100)
    AlphaValue(120)
    ConstantAlphaModifier(-12)
    EndAttack()
    CreateObject('NY_MagicA', -1)
    CreateObject('DIST_TriSwd', -1)
    CreateParticle('nyef_blackptcdel', -1)


@State
def White():
    sprite('vr_white', 30)
    SetZVal(-500)
    BlendMode_Normal()
    AlphaValue(0)
    ConstantAlphaModifier(20)
    ScreenPosition(1)
    SetPosXByScreenPer(50)
    SetPosYByScreenPer(-50)
    AbsoluteY(-450000)
    XPositionRelativeFacingAbsolute(640000)
    Size(4000)
    sprite('vr_white', 30)
    ConstantAlphaModifier(-10)


@State
def StartWhite():
    sprite('vr_white', 40)
    SetZVal(-500)
    BlendMode_Normal()
    AlphaValue(0)
    ConstantAlphaModifier(20)
    ScreenPosition(1)
    SetPosXByScreenPer(50)
    SetPosYByScreenPer(-50)
    AbsoluteY(-450000)
    XPositionRelativeFacingAbsolute(640000)
    Size(4000)
    sprite('vr_white', 30)
    ConstantAlphaModifier(-10)


@State
def FinishWhite():
    sprite('vr_white', 30)
    SetZVal(-500)
    BlendMode_Normal()
    AlphaValue(255)
    ScreenPosition(1)
    SetPosXByScreenPer(50)
    SetPosYByScreenPer(-50)
    AbsoluteY(-450000)
    XPositionRelativeFacingAbsolute(640000)
    Size(4000)
    sprite('vr_white', 30)
    ConstantAlphaModifier(-10)


@State
def NY_AHAnime():

    def upon_IMMEDIATE():
        ScreenPosition(1)
        SetPosXByScreenPer(50)
        AbsoluteY(-450000)
        XPositionRelativeFacingAbsolute(640000)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageInterval(1)
        AfterimageCount(3)
        AfterimageMask_1(0, 255, 0, 0)
        AfterimageMask_2(0, 0, 0, 0)
        AfterimageSize_1(1010)
        AfterimageSize_2(1010)
        FaceRight()
    sprite('null', 40)
    sprite('ny450_a00', 4)
    Size(900)
    SetScaleSpeed(1)
    setGravity(-2)
    AlphaValue(0)
    ConstantAlphaModifier(10)
    Voiceline('rm292')
    if SLOT_43:
        Mouth(13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409,
            13411, 13409, 13411, 13409, 13411, 13409, 99, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Mouth(13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409,
            13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    CreateObject('Astral3DFunnel', -1)
    sprite('ny450_a01', 4)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    sprite('ny450_a00', 4)
    sprite('ny450_a01', 4)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    sprite('ny450_a00', 4)
    CommonSE('019_quake_0')
    sprite('ny450_a01', 4)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    sprite('ny450_a00', 4)
    sprite('ny450_a01', 4)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    if SLOT_43:
        Mouth(13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409,
            13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Mouth(12643, 24886, 25396, 24884, 25396, 24884, 25396, 24884, 25396,
            24884, 25396, 24884, 25396, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ny450_a00', 4)
    CommonSE('019_quake_0')
    sprite('ny450_a01', 4)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    sprite('ny450_a00', 4)
    sprite('ny450_a01', 4)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    sprite('ny450_a00', 4)
    CommonSE('019_quake_1')
    sprite('ny450_a01', 4)
    if SLOT_43:
        Mouth(13409, 13923, 13409, 13923, 13409, 13923, 13409, 13923, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Mouth(13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409,
            13411, 13409, 13411, 13409, 13411, 13409, 13411, 13409, 13411, 
            13409, 14179, 13409, 14179, 13409, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    sprite('ny450_a00', 4)
    sprite('ny450_a01', 4)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    sprite('ny450_a00', 4)
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    sprite('ny450_a01', 4)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    if SLOT_43:
        Mouth(13409, 13923, 13409, 13923, 13153, 25392, 14389, 13409, 13667,
            13921, 12643, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        pass
    sprite('ny450_a00', 4)
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    sprite('ny450_a01', 4)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    sprite('ny450_a00', 4)
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    sprite('ny450_a01', 4)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    sprite('ny450_a00', 4)
    sprite('ny450_a00', 4)
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    if SLOT_43:
        Mouth(14433, 13155, 24882, 25399, 24886, 25398, 24886, 25398, 54, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        pass
    sprite('ny450_a01', 4)
    sprite('ny450_a02', 4)
    sprite('ny450_a03', 4)
    sprite('ny450_a00', 4)
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    sprite('ny450_a04', 7)
    Size(1000)
    SetScaleSpeed(0)
    setGravity(1)
    sprite('ny450_a05', 7)
    sprite('ny450_a06', 7)
    sprite('ny450_a07', 7)
    CommonSE('019_quake_0')
    sprite('ny450_a08', 7)
    sprite('ny450_a09', 5)
    CommonSE('019_quake_1')
    sprite('ny450_a10', 5)
    sprite('ny450_a11', 5)
    sprite('ny450_a12', 5)
    sprite('ny450_a13', 5)
    sprite('ny450_a14', 5)
    sprite('ny450_a15', 5)
    sprite('ny450_a16', 5)
    PrivateSE('nyse_27')
    sprite('ny450_a17', 6)
    sprite('ny450_a19', 6)
    PrivateSE('nyse_27')
    sprite('ny450_a20', 6)
    sprite('ny450_a21', 6)
    PrivateSE('nyse_27')
    sprite('ny450_a22', 4)
    setGravity(0)
    PrivateSE('nyse_27')
    sprite('ny450_a23', 4)
    sprite('ny450_a24', 4)
    sprite('ny450_a22', 4)
    sprite('ny450_a23', 4)
    PrivateSE('nyse_27')
    sprite('ny450_a24', 4)
    sprite('ny450_a22', 4)
    PrivateSE('nyse_27')
    sprite('ny450_a23', 4)
    sprite('ny450_a24', 4)
    PrivateSE('nyse_27')
    sprite('ny450_a22', 4)
    sprite('ny450_a23', 4)
    setGravity(-1)
    YAccel(80)
    sprite('ny450_a24', 4)
    YAccel(80)
    sprite('ny450_a22', 4)
    YAccel(80)
    sprite('ny450_a23', 4)
    YAccel(80)
    sprite('ny450_a24', 4)
    YAccel(80)
    sprite('ny450_a22', 4)
    YAccel(80)
    sprite('ny450_a23', 4)
    YAccel(80)
    sprite('ny450_a24', 4)
    YAccel(0)
    sprite('ny450_a22', 4)
    PrivateSE('nyse_04')
    CommonSE('019_quake_1')
    PrivateSE('nyse_30')
    sprite('ny450_a23', 4)
    sprite('ny450_a24', 4)
    sprite('ny450_a22', 4)
    CommonSE('015_blaze_1')
    PrivateSE('nyse_04')
    sprite('ny450_a23', 4)
    sprite('ny450_a24', 4)
    sprite('ny450_a22', 4)
    CommonSE('015_blaze_1')
    PrivateSE('nyse_04')
    CommonSE('019_quake_0')
    sprite('ny450_a23', 4)
    sprite('ny450_a24', 4)
    sprite('ny450_a22', 4)
    CommonSE('015_blaze_1')
    sprite('ny450_a23', 4)
    sprite('ny450_a24', 4)
    sprite('ny450_a22', 4)
    CommonSE('015_blaze_1')
    CommonSE('019_quake_0')
    sprite('ny450_a23', 4)
    sprite('ny450_a24', 4)
    sprite('ny450_a22', 4)
    CommonSE('015_blaze_1')
    sprite('ny450_a23', 4)
    sprite('ny450_a24', 4)
    sprite('ny450_a22', 4)
    CommonSE('015_blaze_1')
    CommonSE('019_quake_0')
    sprite('ny450_a23', 4)
    sprite('ny450_a24', 4)
    sprite('ny450_a22', 4)
    CommonSE('015_blaze_1')
    setGravity(0)
    sprite('ny450_a25', 5)
    physicsYImpulse(0)
    setGravity(0)
    Voiceline('rm293')
    CommonSE('011_spin_0')
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    sprite('ny450_a23', 4)
    CommonSE('011_spin_0')
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    sprite('ny450_a26', 4)
    sprite('ny450_a27', 4)
    sprite('ny450_a28', 4)
    sprite('ny450_a29', 4)
    sprite('ny450_a30', 4)
    ConstantAlphaModifier(-10)
    sprite('ny450_a31', 30)


@State
def Astral3DFunnel():

    def upon_IMMEDIATE():
        SetZVal(-1000)
        BlendMode_Add()
        ScreenPosition(1)
        SetPosYByScreenPer(-50)
        SetPosXByScreenPer(50)
        AddY(-1600000)
    sprite('null', 180)
    Eff3DEffect('nyah_funnel.DIG', 'nyah_funnel_mt_000.mmot')
    AlphaValue(0)
    ConstantAlphaModifier(10)
    SetScaleSpeed(1)
    Size(1400)
    sprite('null', 7)
    AddY(-15000)
    AddScale(100)
    physicsYImpulse(-2500)
    sprite('null', 7)
    AddY(-15000)
    AddScale(50)
    sprite('null', 7)
    AddScale(100)
    sprite('null', 7)
    sprite('null', 7)
    sprite('null', 5)
    sprite('null', 60)
    SetScaleSpeed(50)
    physicsYImpulse(-40000)


@State
def AstrakFinishPtc():

    def upon_IMMEDIATE():
        LinkParticle('nyef_ashfinish')
        Flip()
        ScreenPosition(1)
        SetPosXByScreenPer(50)
        AbsoluteY(0)
    sprite('null', 32767)


@State
def AstralSword():

    def upon_IMMEDIATE():
        AttackDefaults_AstralHeatProjectile()
        DefeatOpponentBehavior(3)
        Hitstop(30)
        AttackDirection(3)
        uponSendToLabel(LANDING, 0)
        Flip()
        AbsoluteY(2000000)
        AddX(1600000)
        Size(3000)
    sprite('vr_sword', 32767)
    physicsXImpulse(-100000)
    physicsYImpulse(-100000)
    label(0)
    sprite('vr_sword', 130)
    HitAnywhere(1)
    EndMomentum(1)
    ScreenShake(200000, 0)
    sprite('vr_sword', 20)
    PrivateSE('nyse_04')
    BlendMode_Normal()
    ConstantAlphaModifier(-30)
    ParticleSize(4000)
    CallCustomizableParticle('nyef_sumB', 0)
    ParticleSize(4000)
    CallCustomizableParticle('nyef_sumB', 1)
    ParticleSize(4000)
    CallCustomizableParticle('nyef_sumB', 2)
    ParticleSize(4000)
    CallCustomizableParticle('nyef_sumB', 3)
    ParticleSize(4000)
    CallCustomizableParticle('nyef_sumB', 4)
    ParticleSize(4000)
    CallCustomizableParticle('nyef_sumB', 5)
    ParticleSize(4000)
    CallCustomizableParticle('nyef_sumB', 6)


@State
def AstralLookAtMeDummy():
    sprite('null', 2000)
    CameraControlEnable(1)
    CameraFast(1)
    TeleportToObject(22)
    AbsoluteY(0)
    RemoveOnCallStateEnd(3)


@State
def NY_AirCurveSword13Mode():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
        AlphaValue(255)
        RotationAngle(-10000)
        EnableAfterimage(1)
        AfterimageBlendMode(1)
        AfterimageCount(6)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AttackLevel_(3)
        Damage(1000)
        SameMoveProration(85)
        UseSlashHitspark(1)
        CHAirUntechableTime(40)
        AddX(160000)
        AddY(380000)
        AttackP1(80)
        HitOverhead(2)
        GroundedHitstunAnimation(9)
        AirPushbackX(23000)
        AirPushbackY(-35000)
        YImpulseBeforeWallbounce(0)
        AirUntechableTime(40)
        HardKnockdown(10)
    sprite('vrnyef_swdg00', 2)
    AddScale(-280)
    SetScaleSpeed(10)
    CreateParticle('nyef_sumB', 0)
    CreateParticle('nyef_sumB', 1)
    CreateParticle('nyef_sumB', 2)
    CreateParticle('nyef_sumB', 3)
    CreateParticle('nyef_sumB', 4)
    CreateParticle('nyef_sumB', 5)
    PrivateSE('nyse_30')
    sprite('vrnyef_swdg01', 2)
    sprite('vrnyef_swdg01', 2)
    sprite('vrnyef_swdg01', 1)
    AddScale(20)
    AddRotationPerFrame(3000)
    SetAcceleration(300)
    SetScaleSpeed(50)
    StartMultihit()
    CreateParticle('nyef_sumB', 5)
    sprite('vrnyef_swdg01', 1)
    CreateParticle('nyef_sumB', 5)
    sprite('vrnyef_swdg02', 1)
    CreateParticle('nyef_sumB', 5)
    PrivateSE('nyse_31')
    sprite('vrnyef_swdg03', 1)
    CreateParticle('nyef_sumB', 5)
    sprite('vrnyef_swdg04', 4)
    SetScaleSpeed(0)
    AddRotationPerFrame(500)
    ConstantAlphaModifier(-5)
    CreateParticle('nyef_sumB', 5)
    sprite('vrnyef_swdg05', 4)
    AlphaValue(200)
    ConstantAlphaModifier(-50)
    CreateParticle('nyef_sumB', 0)
    CreateParticle('nyef_sumB', 1)
    CreateParticle('nyef_sumB', 2)
    CreateParticle('nyef_sumB', 3)
    CreateParticle('nyef_sumB', 4)
    CreateParticle('nyef_sumB', 5)
    CreateParticle('nyef_sumBlight', 5)


@State
def NY_AirCurveSword11Mode():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(1000)
        if SLOT_137:
            DamageMultiplier(80)
        UseSlashHitspark(1)
        CHAirUntechableTime(40)
        AttackP1(80)
        HitOverhead(2)
        GroundedHitstunAnimation(9)
        AirPushbackY(-30000)
        AirUntechableTime(40)
        HardKnockdown(15)
        Hitstop(7)
        AutoHitStopSending(1)
        StarterRating(2)
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
        AlphaValue(255)
        RotationAngle(-10000)
        EnableAfterimage(1)
        AfterimageBlendMode(1)
        AfterimageCount(6)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AddX(-25000)
        AddY(450000)
        Size(1150)

        def upon_32():
            Size(1200)
            AirPushbackY(-60000)
            YImpulseBeforeWallbounce(0)
            GroundBounce(1)
            BouncePercentage(30)
            AirHitstunAfterWallbounce(40)

        def upon_OPPONENT_HIT_OR_BLOCK():
            ScreenShake(3000, 6000)
        SameMoveProration(1)
    sprite('vrnyef_swdg00', 4)
    Visibility(1)
    CreateParticle('nyef_sumB', 0)
    CreateParticle('nyef_sumB', 1)
    CreateParticle('nyef_sumB', 2)
    CreateParticle('nyef_sumB', 3)
    CreateParticle('nyef_sumB', 4)
    CreateParticle('nyef_sumB', 5)
    PrivateSE('nyse_28')
    sprite('vrnyef_swdg00', 2)
    Visibility(0)
    AddScale(-280)
    SetScaleSpeed(10)
    sprite('vrnyef_swdg01', 2)
    sprite('vrnyef_swdg01', 1)
    AddScale(20)
    AddRotationPerFrame(3000)
    SetAcceleration(300)
    SetScaleSpeed(25)
    StartMultihit()
    CreateParticle('nyef_sumB', 5)
    sprite('vrnyef_swdg01', 1)
    CreateParticle('nyef_sumB', 5)
    sprite('vrnyef_swdg02', 1)
    CreateParticle('nyef_sumB', 5)
    PrivateSE('nyse_33')
    sprite('vrnyef_swdg06', 2)
    CreateParticle('nyef_sumB', 5)
    sprite('vrnyef_swdg07', 2)
    SetScaleSpeed(0)
    AddRotationPerFrame(500)
    ConstantAlphaModifier(-5)
    CreateParticle('nyef_sumB', 5)
    sprite('vrnyef_swdg08', 1)
    ConstantAlphaModifier(-50)
    CreateParticle('nyef_sumB', 0)
    CreateParticle('nyef_sumB', 1)
    CreateParticle('nyef_sumB', 2)
    CreateParticle('nyef_sumB', 3)
    CreateParticle('nyef_sumB', 4)
    CreateParticle('nyef_sumB', 5)
    CreateParticle('nyef_sumBlight', 5)
    sprite('vrnyef_swdg08', 3)


@State
def BottomSword11ModeOD():
    sprite('null', 240)
    CreateObject('BottomSword11Mode', -1)
    ObjectUpon(STATE_END, 32)
    CreateObject('BottomSword11Mode_Add', -1)


@State
def BottomSword11Mode():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        PaletteIndex(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(4)
        AfterimageColor_1(128, 128, 128, 90)
        AfterimageColor_2(128, 128, 128, 90)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AttackLevel_(3)
        Damage(400)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        AttackP2(79)
        SingleProration(1)
        AirPushbackY(10000)
        AirUntechableTime(30)
        Hitstop(4)
        MoveAttributes(0, 0, 0, 1, 0)
        HardKnockdown(1)
        UseSlashHitspark(1)
        ChipPercentage(20)
        SameMoveProration(1)

        def upon_32():
            VoodooDamageMultiplier(2)
        AddY(-32000)
        AddX(750000)
        if not SLOT_IsFacingRight:
            SLOT_40 >= 0
            SLOT_51 = SLOT_0
        else:
            SLOT_40 <= -1
            SLOT_51 = SLOT_0
        if SLOT_51:
            PushbackX(6000)
            AirPushbackX(2000)
            physicsXImpulse(24000)
            SetAcceleration(1000)
        else:
            FlipOnHit(1)
            PushbackX(-6000)
            AirPushbackX(-2000)
            physicsXImpulse(-24000)
            SetAcceleration(-1000)
            Flip()
        PushSpeedX()
        PushAcceleration()
        EndMomentum(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            clearUponHandler(OPPONENT_HIT_OR_BLOCK)
            WallCollisionDetection(1)
            XImpulseAcceleration(0)
            SetActionMark(3)
            sendToLabel(1)
        HitsPerCall(1, 0, 0, 0, 1, 0, 1, 1)
        uponSendToLabel(54, 580)
        ContinueState(120)
        SLOT_5 = 1

        def upon_STATE_END():
            SLOT_5 = 0
    sprite('null', 1)
    CommonSE('022_magiccircle_b')
    sprite('vrnyef_swdf03', 8)
    AttackOff()
    Visibility(1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    ParticleSize(1500)
    CallCustomizableParticle('nyef_bottomswdptc00', -1)
    ParticleSize(3000)
    CallCustomizableParticle('nyef_bottomswd', -1)
    sprite('vrnyef_swdf03', 8)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    ParticleSize(1500)
    CallCustomizableParticle('nyef_bottomswdptc00', -1)
    ParticleSize(3000)
    CallCustomizableParticle('nyef_bottomswd', -1)
    sprite('null', 1)
    Visibility(0)
    label(0)
    sprite('vrnyef_swdf04', 1)
    CommonSE('006_swing_blade_2')
    RotationAngle(0)
    AddRotationPerFrame(0)
    ParticleSize(2400)
    CallCustomizableParticle('nyef_bottomswd', -1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf05', 2)
    RefreshMultihit()
    PopSpeedX()
    PopAcceleration()
    sprite('vrnyef_swdf06', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf07', 2)
    sprite('vrnyef_swdf08', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf09', 2)
    sprite('vrnyef_swdf00', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf01', 1)
    sprite('vrnyef_swdf02', 1)
    sprite('vrnyef_swdf03', 1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrnyef_swdf00', 1)
    PerAcceleration(200)
    CommonSE('006_swing_blade_2')
    AttackOff()
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf01', 1)
    sprite('vrnyef_swdf02', 1)
    sprite('vrnyef_swdf03', 1)
    sprite('vrnyef_swdf04', 1)
    ParticleSize(2400)
    CallCustomizableParticle('nyef_bottomswd', -1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf05', 1)
    sprite('vrnyef_swdf06', 1)
    sprite('vrnyef_swdf07', 1)
    label(2)
    sprite('vrnyef_swdf00', 1)
    RefreshMultihit()
    if SLOT_2 == 1:
        HardKnockdown(0)
    XImpulseAcceleration(50)
    PerAcceleration(50)
    CommonSE('006_swing_blade_2')
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf01', 1)
    sprite('vrnyef_swdf02', 1)
    sprite('vrnyef_swdf03', 1)
    sprite('vrnyef_swdf04', 1)
    ParticleSize(2400)
    CallCustomizableParticle('nyef_bottomswd', -1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf05', 1)
    sprite('vrnyef_swdf06', 1)
    sprite('vrnyef_swdf07', 1)
    AddActionMark(-1)
    if not SLOT_2:
        notConditionalSendToLabel(580)
    loopRest()
    gotoLabel(2)
    label(580)
    sprite('keep', 30)
    EndMomentum(1)
    AttackOff()
    ConstantAlphaModifier(-20)
    ParticleSize(1500)
    CallCustomizableParticle('nyef_bottomswdptc00', -1)
    ParticleSize(3000)
    CallCustomizableParticle('nyef_bottomswd', -1)
    ParticleSize(2400)
    CallCustomizableParticle('nyef_bottomswd', -1)


@State
def BottomSword11Mode_Add():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        PaletteIndex(1)
        BlendMode_Normal()
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(4)
        AfterimageColor_1(128, 128, 128, 90)
        AfterimageColor_2(128, 128, 128, 90)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        AttackLevel_(3)
        Damage(400)
        if SLOT_137:
            DamageMultiplier(80)
        AttackP1(80)
        SingleProration(1)
        AirPushbackY(10000)
        AirUntechableTime(30)
        Hitstop(4)
        MoveAttributes(0, 0, 0, 1, 0)
        HardKnockdown(1)
        UseSlashHitspark(1)
        ChipPercentage(20)
        SameMoveProration(1)
        VoodooDamageMultiplier(2)
        AddY(-32000)
        AddX(750000)
        if not SLOT_IsFacingRight:
            SLOT_40 >= 0
            SLOT_51 = SLOT_0
        else:
            SLOT_40 <= -1
            SLOT_51 = SLOT_0
        if not SLOT_51:
            PushbackX(6000)
            AirPushbackX(2000)
            physicsXImpulse(24000)
            SetAcceleration(1000)
        else:
            FlipOnHit(1)
            PushbackX(-6000)
            AirPushbackX(-2000)
            physicsXImpulse(-24000)
            SetAcceleration(-1000)
            Flip()
        PushSpeedX()
        PushAcceleration()
        EndMomentum(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            clearUponHandler(OPPONENT_HIT_OR_BLOCK)
            WallCollisionDetection(1)
            XImpulseAcceleration(0)
            SetActionMark(3)
            sendToLabel(1)
        HitsPerCall(1, 0, 0, 0, 1, 0, 1, 1)
        uponSendToLabel(54, 580)
        ContinueState(120)
        SLOT_5 = 1

        def upon_STATE_END():
            SLOT_5 = 0
    sprite('null', 1)
    CommonSE('022_magiccircle_b')
    sprite('vrnyef_swdf03', 8)
    AttackOff()
    Visibility(1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    ParticleSize(1500)
    CallCustomizableParticle('nyef_bottomswdptc00', -1)
    ParticleSize(3000)
    CallCustomizableParticle('nyef_bottomswd', -1)
    sprite('vrnyef_swdf03', 8)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    ParticleSize(1500)
    CallCustomizableParticle('nyef_bottomswdptc00', -1)
    ParticleSize(3000)
    CallCustomizableParticle('nyef_bottomswd', -1)
    sprite('null', 1)
    Visibility(0)
    label(0)
    sprite('vrnyef_swdf04', 1)
    CommonSE('006_swing_blade_2')
    RotationAngle(0)
    AddRotationPerFrame(0)
    ParticleSize(2400)
    CallCustomizableParticle('nyef_bottomswd', -1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf05', 2)
    RefreshMultihit()
    PopSpeedX()
    PopAcceleration()
    sprite('vrnyef_swdf06', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf07', 2)
    sprite('vrnyef_swdf08', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf09', 2)
    sprite('vrnyef_swdf00', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf01', 1)
    sprite('vrnyef_swdf02', 1)
    sprite('vrnyef_swdf03', 1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrnyef_swdf00', 1)
    PerAcceleration(200)
    CommonSE('006_swing_blade_2')
    AttackOff()
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf01', 1)
    sprite('vrnyef_swdf02', 1)
    sprite('vrnyef_swdf03', 1)
    sprite('vrnyef_swdf04', 1)
    ParticleSize(2400)
    CallCustomizableParticle('nyef_bottomswd', -1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf05', 1)
    sprite('vrnyef_swdf06', 1)
    sprite('vrnyef_swdf07', 1)
    label(2)
    sprite('vrnyef_swdf00', 1)
    RefreshMultihit()
    if SLOT_2 == 1:
        HardKnockdown(0)
    XImpulseAcceleration(50)
    PerAcceleration(50)
    CommonSE('006_swing_blade_2')
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf01', 1)
    sprite('vrnyef_swdf02', 1)
    sprite('vrnyef_swdf03', 1)
    sprite('vrnyef_swdf04', 1)
    ParticleSize(2400)
    CallCustomizableParticle('nyef_bottomswd', -1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf05', 1)
    sprite('vrnyef_swdf06', 1)
    sprite('vrnyef_swdf07', 1)
    AddActionMark(-1)
    if not SLOT_2:
        notConditionalSendToLabel(580)
    loopRest()
    gotoLabel(2)
    label(580)
    sprite('keep', 30)
    EndMomentum(1)
    AttackOff()
    ConstantAlphaModifier(-20)
    ParticleSize(1500)
    CallCustomizableParticle('nyef_bottomswdptc00', -1)
    ParticleSize(3000)
    CallCustomizableParticle('nyef_bottomswd', -1)
    ParticleSize(2400)
    CallCustomizableParticle('nyef_bottomswd', -1)


@State
def BottomSword13Mode():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        CancelIfPlayerHit(3)
        PaletteIndex(1)
        AddX(200000)
        AddY(-32000)
        AlphaValue(160)
        ContinueState(120)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(5)
        AfterimageColor_1(128, 255, 255, 255)
        AfterimageColor_2(255, 0, 0, 0)
        AfterimageSize_1(1100)
        AfterimageSize_2(1200)
        AttackLevel_(3)
        Damage(900)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AttackP1(95)
        SameMoveProration(10)
        UseSlashHitspark(1)
        MoveAttributes(0, 0, 0, 1, 0)

        def upon_32():
            CreateParticle('nyef_bottomswd', 0)
            CreateParticle('nyef_bottomswd', 1)
            CreateParticle('nyef_bottomswd', 2)
            ParticleSize(1500)
            CallCustomizableParticle('nyef_bottomswdptc00', -1)
            ParticleSize(3000)
            CallCustomizableParticle('nyef_bottomswd', -1)
            AirHitstunAnimation(11)
            GroundedHitstunAnimation(11)
            PushbackX(40000)
            AirPushbackX(35000)
            AirPushbackY(11000)
            YImpulseBeforeWallbounce(1000)
            AirUntechableTime(35)

            def upon_OPPONENT_HIT():
                if CheckCondition(12400):
                    AirPushbackY(10000)
            physicsXImpulse(40000)

        def upon_33():
            Damage(980)
            AirPushbackY(17000)
            CHAirPushbackY(32000)
            AirUntechableTime(25)
            CHAirUntechableTime(50)
            AddX(620000)
            Flip()
            physicsXImpulse(25000)
            CreateParticle('nyef_bottomswd', 0)
            CreateParticle('nyef_bottomswd', 1)
            CreateParticle('nyef_bottomswd', 2)
            ParticleSize(1500)
            CallCustomizableParticle('nyef_bottomswdptc00', -1)
            ParticleSize(3000)
            CallCustomizableParticle('nyef_bottomswd', -1)

        def upon_45():
            if SLOT_StateDuration > 70:
                CollideWithWall(1)
        HitsPerCall(1, 0, 1, 1, 1, 0, 1, 1)
        uponSendToLabel(54, 580)
    sprite('vrnyef_swdf03', 6)
    RotationAngle(-90000)
    AddRotationPerFrame(10000)
    ConstantAlphaModifier(30)
    CommonSE('022_magiccircle_b')
    sprite('vrnyef_swdf03', 3)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    label(0)
    sprite('vrnyef_swdf04', 1)
    CommonSE('006_swing_blade_2')
    RotationAngle(0)
    AddRotationPerFrame(0)
    ParticleSize(2400)
    CallCustomizableParticle('nyef_bottomswd', -1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf05', 2)
    sprite('vrnyef_swdf06', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf07', 2)
    sprite('vrnyef_swdf08', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf09', 2)
    sprite('vrnyef_swdf00', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf01', 1)
    sprite('vrnyef_swdf02', 1)
    sprite('vrnyef_swdf03', 1)
    loopRest()
    gotoLabel(0)
    label(580)
    sprite('keep', 30)
    ParticleSize(1500)
    CallCustomizableParticle('nyef_bottomswdptc00', -1)
    ParticleSize(3000)
    CallCustomizableParticle('nyef_bottomswd', -1)
    ParticleSize(2400)
    CallCustomizableParticle('nyef_bottomswd', -1)
    XImpulseAcceleration(50)
    physicsYImpulse(0)
    AddRotationPerFrame(0)
    ConstantAlphaModifier(-20)
    AttackOff()


@State
def SummonBottomSwordHold():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        PaletteIndex(1)
        SetPosXByScreenPer(105)
        AddY(-64000)
        SetScaleX(-1000)
        AlphaValue(0)
        ContinueState(120)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(5)
        AfterimageColor_1(128, 255, 255, 255)
        AfterimageColor_2(255, 0, 0, 0)
        AfterimageSize_1(1100)
        AfterimageSize_2(1200)
        AttackLevel_(3)
        Damage(900)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(28)
        AirPushbackX(-3000)
        PushbackX(-18000)
        CollideWithWall(1)
        HitsPerCall(1, 0, 1, 1, 1, 0, 1, 1)
        uponSendToLabel(54, 580)
    sprite('vrnyef_swdf03', 6)
    RotationAngle(-90000)
    AddRotationPerFrame(-10000)
    physicsXImpulse(-30000)
    ConstantAlphaModifier(30)
    StartMultihit()
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    ParticleSize(1500)
    CallCustomizableParticle('nyef_bottomswdptc00', -1)
    ParticleSize(3000)
    CallCustomizableParticle('nyef_bottomswd', -1)
    sprite('vrnyef_swdf03', 3)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    label(0)
    sprite('vrnyef_swdf04', 1)
    RotationAngle(0)
    AddRotationPerFrame(0)
    ParticleSize(2400)
    CallCustomizableParticle('nyef_bottomswd', -1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf05', 2)
    sprite('vrnyef_swdf06', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf07', 2)
    sprite('vrnyef_swdf08', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf09', 2)
    sprite('vrnyef_swdf00', 2)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_swdf01', 1)
    sprite('vrnyef_swdf02', 1)
    sprite('vrnyef_swdf03', 1)
    loopRest()
    gotoLabel(0)
    label(580)
    sprite('keep', 30)
    ParticleSize(1500)
    CallCustomizableParticle('nyef_bottomswdptc00', -1)
    ParticleSize(3000)
    CallCustomizableParticle('nyef_bottomswd', -1)
    ParticleSize(2400)
    CallCustomizableParticle('nyef_bottomswd', -1)
    physicsXImpulse(0)
    physicsYImpulse(0)
    AddRotationPerFrame(0)
    ConstantAlphaModifier(-20)


@State
def SummonDDBigSwordBoss():
    sprite('null', 20)
    IgnoreScreenfreeze(1)
    CreateObject('SummonDDBigSword', -1)
    AddX(150000)
    sprite('null', 20)
    CreateObject('SummonDDBigSword', -1)
    AddX(150000)
    sprite('null', 20)
    CreateObject('SummonDDBigSword', -1)
    AddX(150000)
    sprite('null', 20)
    CreateObject('SummonDDBigSword', -1)
    AddX(150000)


@State
def SummonDDBigSwordOverDrive():
    sprite('null', 15)
    IgnoreScreenfreeze(1)
    CreateObject('SummonDDBigSwordOD', -1)
    AddX(150000)
    sprite('null', 15)
    CreateObject('SummonDDBigSwordOD', -1)
    AddX(150000)
    sprite('null', 15)
    CreateObject('SummonDDBigSwordOD', -1)
    AddX(150000)
    sprite('null', 15)
    CreateObject('SummonDDBigSwordOD', -1)
    ObjectUpon(STATE_END, 32)
    AddX(150000)


@State
def SummonDDBigSword():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        AddX(256000)
        AddY(640000)
        SetZVal(-1)
        AlphaValue(0)
        WallCollisionDetection(1)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageInterval(1)
        AfterimageCount(3)
        AfterimageColor_1(0, 255, 0, 0)
        AfterimageColor_2(255, 0, 0, 0)
        AfterimageSize_1(1030)
        AfterimageSize_2(1040)
        AttackLevel_(4)
        Damage(2400)
        if SLOT_137:
            DamageMultiplier(80)
        MinimumDamage(40)
        AttackP1(70)
        AttackP2(82)
        HitOverhead(2)
        GroundedHitstunAnimation(9)
        AirUntechableTime(100)
        YImpulseBeforeWallbounce(0)
        GroundBounce(1)
        BouncePercentage(50)
        UseSlashHitspark(1)
        StarterRating(2)
        CopyFromRightToLeft(23, 2, 51, 3, 2, 36)
        if SLOT_51:
            AddX(70000)
            AirPushbackY(-60000)
            HardKnockdown(1)
        else:
            AirPushbackY(-80000)
            CHAirPushbackY(-100000)
            HitAirUnblockable(3)
    sprite('vrnyef_ddbigswd00', 41)
    CreateObject('NY_SumBigSword', -1)
    CreateObject('SummonDDBigSwordSub', -1)
    ConstantAlphaModifier(10)
    AddY(512000)
    physicsYImpulse(-1000)
    CreateParticle('nyef_bottomswd', -1)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_ddbigswd01', 1)
    AddY(-200000)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    ScreenShake(0, 30000)
    PrivateSE('nyse_04')
    sprite('vrnyef_ddbigswd02', 1)
    AddY(-150000)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_ddbigswd03', 1)
    AddY(-50000)
    CreateParticle('rmef_sumDDshock', 104)
    CreateParticle('nyef_sumDDshocklight00', 0)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_ddbigswd04', 8)
    AlphaValue(255)
    SetScaleSpeed(1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    sprite('vrnyef_ddbigswd05', 25)
    physicsYImpulse(2000)
    ConstantAlphaModifier(-10)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)


@State
def SummonDDBigSwordOD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        TeleportToObject(22)
        CopyFromRightToLeft(23, 2, 23, 3, 2, 23)
        AddY(640000)
        SetZVal(-1)
        AlphaValue(0)
        Size(1250)
        WallCollisionDetection(1)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageInterval(1)
        AfterimageCount(3)
        AfterimageColor_1(0, 255, 0, 0)
        AfterimageColor_2(255, 0, 0, 0)
        AfterimageSize_1(1030)
        AfterimageSize_2(1040)
        AttackLevel_(4)
        Damage(2800)
        if SLOT_137:
            DamageMultiplier(80)
        MinimumDamage(45)
        AttackP1(70)
        AttackP2(82)
        HitOverhead(2)
        GroundedHitstunAnimation(9)
        AirUntechableTime(100)
        YImpulseBeforeWallbounce(0)
        GroundBounce(1)
        BouncePercentage(50)
        UseSlashHitspark(1)
        StarterRating(2)
        AttackType(4)
        CopyFromRightToLeft(23, 2, 51, 3, 2, 36)
        if SLOT_51:
            AddX(70000)
            AirPushbackY(-60000)
            HardKnockdown(1)
        else:
            AirPushbackY(-80000)
            CHAirPushbackY(-100000)
            HitAirUnblockable(3)
    sprite('vrnyef_ddbigswd00', 41)
    CreateObject('NY_SumBigSword', -1)
    CreateObject('SummonDDBigSwordSub', -1)
    if not SLOT_51:
        ObjectUpon(STATE_END, 32)
        AddY(150000)
    ConstantAlphaModifier(10)
    AddY(512000)
    physicsYImpulse(-1000)
    CreateParticle('nyef_bottomswd', -1)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_ddbigswd01', 1)
    AddY(-200000)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    ScreenShake(0, 30000)
    PrivateSE('nyse_04')
    sprite('vrnyef_ddbigswd02', 1)
    AddY(-150000)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_ddbigswd03', 1)
    AddY(-50000)
    CreateParticle('rmef_sumDDshock', 104)
    CreateParticle('nyef_sumDDshocklight00', 0)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_ddbigswd04', 8)
    AlphaValue(255)
    SetScaleSpeed(1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    sprite('vrnyef_ddbigswd05', 25)
    physicsYImpulse(2000)
    ConstantAlphaModifier(-10)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)


@State
def SummonDDBigSwordSub():

    def upon_IMMEDIATE():
        IgnorePauses(2)
        E0EAEffectScale(2)
        PaletteIndex(1)
        SetZVal(-5)
        ContinueState(120)
        AlphaValue(0)
        WallCollisionDetection(1)
        EnableAfterimage(0)
        AfterimageBlendMode(2)
        AfterimageInterval(1)
        AfterimageCount(5)
        AfterimageColor_1(0, 255, 0, 0)
        AfterimageColor_2(255, 0, 0, 0)
        AfterimageSize_1(1020)
        AfterimageSize_2(1050)

        def upon_32():
            AddY(150000)
    sprite('vrnyef_ddbigswdb00', 41)
    ConstantAlphaModifier(10)
    AddY(512000)
    physicsYImpulse(-1000)
    sprite('vrnyef_ddbigswdb01', 1)
    AddY(-200000)
    sprite('vrnyef_ddbigswdb02', 1)
    AddY(-150000)
    sprite('vrnyef_ddbigswdb03', 1)
    AddY(-50000)
    sprite('vrnyef_ddbigswdb04', 8)
    AlphaValue(255)
    SetScaleSpeed(1)
    sprite('vrnyef_ddbigswdb05', 25)
    physicsYImpulse(2000)
    ConstantAlphaModifier(-10)


@State
def __6CZanzo():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        TurnParticleColorable1(1)
        BlendMode_Add()
        PaletteIndex(1)
        PaletteEffType(1)
        PaletteColor1(14)
        PaletteColor2(209)
        PaletteColor3(210)
        PaletteColor4(2147483898)
    sprite('vrnyef213_f00', 8)
    AlphaValue(0)
    ConstantAlphaModifier(20)
    sprite('vrnyef213_f00', 8)


@State
def __2CZanzo():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
        TurnParticleColorable1(1)
        BlendMode_Add()
        PaletteEffType(1)
        PaletteColor1(10)
        PaletteColor2(209)
        PaletteColor3(210)
        PaletteColor4(2147483898)
    sprite('vrnyef232_f00', 6)
    AlphaValue(0)
    ConstantAlphaModifier(40)
    sprite('vrnyef232_f01', 6)
    ConstantAlphaModifier(-40)


@State
def __8CZanzo():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
        TurnParticleColorable1(1)
        BlendMode_Add()
        PaletteEffType(1)
        PaletteColor1(12)
        PaletteColor2(209)
        PaletteColor3(210)
        PaletteColor4(2147483898)
    sprite('vrnyef252_f00', 4)
    AlphaValue(0)
    ConstantAlphaModifier(20)
    sprite('vrnyef252_f01', 2)
    AlphaValue(255)
    ConstantAlphaModifier(-40)
    sprite('vrnyef252_f02', 4)


@State
def __82CZanzo():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
        TurnParticleColorable1(1)
        BlendMode_Add()
        PaletteEffType(1)
        PaletteColor1(10)
        PaletteColor2(209)
        PaletteColor3(210)
        PaletteColor4(2147483898)
    sprite('vrnyef254_f00', 2)
    AlphaValue(0)
    ConstantAlphaModifier(20)
    sprite('vrnyef254_f01', 2)
    AlphaValue(255)
    ConstantAlphaModifier(-40)
    sprite('vrnyef254_f02', 2)


@State
def __3CZanzo():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
        TurnParticleColorable1(1)
        BlendMode_Add()
        PaletteEffType(1)
        PaletteColor1(12)
        PaletteColor2(209)
        PaletteColor3(210)
        PaletteColor4(2147483898)
    sprite('vrnyef234_f00', 4)
    AlphaValue(0)
    ConstantAlphaModifier(40)
    SetScaleSpeedY(-5)
    sprite('vrnyef234_f00', 5)
    SetScaleSpeed(-5)
    ConstantAlphaModifier(-20)


@State
def rmef413():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        AddX(150000)
        AddY(170000)
    sprite('null', 60)
    LinkParticle('rmef_413')


@State
def rmef413_Zanzo():

    def upon_IMMEDIATE():
        IgnorePauses(3)
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        PaletteIndex(1)
        TurnParticleColorable1(1)
        BlendMode_Add()
        PaletteEffType(1)
        PaletteColor1(10)
        PaletteColor2(209)
        PaletteColor3(210)
        PaletteColor4(2147483898)
        SetScaleX(-1000)
        SetScaleY(-1000)
        AddX(30000)
        AddY(430000)
    sprite('vrnyef254_f00', 2)
    AlphaValue(0)
    ConstantAlphaModifier(64)
    sprite('vrnyef254_f01', 4)
    AlphaValue(255)
    ConstantAlphaModifier(-16)
    sprite('vrnyef254_f02', 2)
    AddX(10000)
    AddY(20000)


@State
def Funnel2C():
    sprite('ny232_fx00', 2)
    sprite('ny232_fx01', 2)
    IgnorePauses(3)
    RemoveOnCallStateEnd(3)
    E0EAEffectPosition(3)
    sprite('ny232_fx02', 2)
    sprite('ny232_fx03', 2)
    sprite('ny232_fx04', 2)
    sprite('ny232_fx05', 2)
    sprite('ny232_fx06', 2)


@Subroutine
def Funnel5CReset():
    IgnorePauses(3)
    E0EAEffectPosition(3)
    RemoveOnCallStateEnd(3)
    AddY(300000)
    AddX(-100000)
    E0EAEffectObjectZ(3)
    SetZVal(1)


@State
def FunnelRevive():

    def upon_IMMEDIATE():
        callSubroutine('Funnel5CReset')
    sprite('ny202_f19', 2)
    sprite('ny202_f20', 2)
    sprite('ny202_f21', 2)
    sprite('ny202_f22', 32767)


@State
def Funnel5CMain():

    def upon_IMMEDIATE():
        callSubroutine('Funnel5CReset')
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
        uponSendToLabel(36, 4)
        uponSendToLabel(37, 5)
        uponSendToLabel(38, 6)
        uponSendToLabel(39, 7)
        uponSendToLabel(40, 8)

        def upon_41():
            clearUponHandler(33)
            clearUponHandler(34)
            clearUponHandler(35)
            clearUponHandler(36)
            clearUponHandler(37)
            clearUponHandler(38)
            clearUponHandler(39)
            clearUponHandler(40)
            sendToLabel(9)

        def upon_32():
            Unknown2064(1)
            TriggerUponForState('Funnel5C_Atk', 41)
    sprite('ny202_f01', 2)
    sprite('ny202_f02', 2)
    sprite('ny202_f03', 2)
    sprite('ny202_f04', 2)
    CreateObject('Funnel5C_Atk', -1)
    ObjectUpon(STATE_END, 33)
    sprite('ny202_f05', 1)
    sprite('ny202_f05', 1)
    sprite('ny202_f06', 1)
    RotationAngle(3000)
    sprite('ny202_f06', 20)
    RotationAngle(0)
    sprite('ny202_f06', 10)
    physicsYImpulse(500)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    loopRest()
    label(2)
    sprite('ny202_f06', 2)
    CreateObject('Funnel5C_Atk', -1)
    ObjectUpon(STATE_END, 34)
    sprite('ny202_f07', 1)
    RotationAngle(3000)
    sprite('ny202_f07', 1)
    RotationAngle(0)
    sprite('ny202_f08', 1)
    RotationAngle(3000)
    sprite('ny202_f08', 20)
    RotationAngle(0)
    sprite('ny202_f08', 10)
    physicsYImpulse(500)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    loopRest()
    label(3)
    sprite('ny202_f08', 2)
    CreateObject('Funnel5C_Atk', -1)
    ObjectUpon(STATE_END, 35)
    sprite('ny202_f09', 1)
    RotationAngle(3000)
    sprite('ny202_f09', 1)
    RotationAngle(0)
    sprite('ny202_f10', 1)
    RotationAngle(3000)
    sprite('ny202_f10', 20)
    RotationAngle(0)
    sprite('ny202_f10', 10)
    physicsYImpulse(500)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    loopRest()
    label(4)
    sprite('ny202_f10', 2)
    CreateObject('Funnel5C_Atk', -1)
    ObjectUpon(STATE_END, 36)
    sprite('ny202_f11', 1)
    RotationAngle(3000)
    sprite('ny202_f11', 1)
    RotationAngle(0)
    sprite('ny202_f12', 1)
    RotationAngle(3000)
    sprite('ny202_f12', 20)
    RotationAngle(0)
    sprite('ny202_f12', 10)
    physicsYImpulse(500)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    loopRest()
    label(5)
    sprite('ny202_f12', 2)
    CreateObject('Funnel5C_Atk', -1)
    ObjectUpon(STATE_END, 37)
    sprite('ny202_f13', 1)
    RotationAngle(3000)
    sprite('ny202_f13', 1)
    RotationAngle(0)
    sprite('ny202_f14', 1)
    RotationAngle(3000)
    sprite('ny202_f14', 20)
    RotationAngle(0)
    sprite('ny202_f14', 10)
    physicsYImpulse(500)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    loopRest()
    label(6)
    sprite('ny202_f14', 2)
    CreateObject('Funnel5C_Atk', -1)
    ObjectUpon(STATE_END, 38)
    sprite('ny202_f15', 1)
    RotationAngle(3000)
    sprite('ny202_f15', 1)
    RotationAngle(0)
    sprite('ny202_f16', 1)
    RotationAngle(3000)
    sprite('ny202_f16', 20)
    RotationAngle(0)
    sprite('ny202_f16', 10)
    physicsYImpulse(500)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    loopRest()
    label(7)
    sprite('ny202_f16', 2)
    CreateObject('Funnel5C_Atk', -1)
    ObjectUpon(STATE_END, 39)
    sprite('ny202_f17', 1)
    RotationAngle(3000)
    sprite('ny202_f17', 1)
    RotationAngle(0)
    sprite('ny202_f18', 1)
    RotationAngle(3000)
    sprite('ny202_f18', 20)
    RotationAngle(0)
    sprite('ny202_f18', 10)
    physicsYImpulse(500)
    ConstantAlphaModifier(-30)
    BlendMode_Normal()
    loopRest()
    label(8)
    sprite('ny202_f18', 2)
    CreateObject('Funnel5C_Atk', -1)
    ObjectUpon(STATE_END, 40)
    loopRest()
    label(9)
    sprite('null', 1)
    ExitState()


@State
def Funnel5C_Atk():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        AttackLevel_(3)
        Damage(160)
        SingleProration(1)
        AirPushbackY(15000)
        AirUntechableTime(21)
        Hitstop(5)
        UseSlashHitspark(1)
        HitsparkSize(600)
        VoodooDamageMultiplier(2)

        def upon_OPPONENT_HIT_OR_BLOCK():
            TriggerUponForState('NmlAtk5C', 32)

        def upon_33():
            HitboxMovement(3000, 250000)

        def upon_34():
            HitboxMovement(3000, 300000)

        def upon_35():
            HitboxMovement(3000, 350000)

        def upon_36():
            HitboxMovement(3000, 400000)

        def upon_37():
            HitboxMovement(3000, 450000)

        def upon_38():
            HitboxMovement(3000, 500000)

        def upon_39():
            HitboxMovement(3000, 550000)

        def upon_40():
            HitboxMovement(3000, 600000)

            def upon_OPPONENT_HIT_OR_BLOCK():
                TriggerUponForState('NmlAtk5C', 33)
        RemoveOnCallStateEnd(3)
        E0EAEffectObjectZ(3)
        SetZVal(-1)
        AddX(-30000)
        AddY(30000)
        RandSpeedX(-4000, 4000)
        RandSpeedY(-4000, 4000)
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 1)
        uponSendToLabel(54, 580)
        AttackOff()

        def upon_45():
            if SLOT_StateDuration > 70:
                clearUponHandler(45)
                ObjectUpon(LANDING, 32)
        Unknown2064(0)

        def upon_41():
            Unknown2064(1)
            CHStateIfCHStart(2)
        CHStateIfCHStart(2)
    sprite('null', 1)
    sprite('null', 1)
    YSpeed(-10000)
    sprite('ny202_f18ex01', 2)
    PrivateSE('nyse_29')
    sprite('ny202_f00atk', 2)
    sprite('ny202_f01atk', 1)
    sprite('ny202_f02atk', 1)
    SetAcceleration(100)
    sprite('ny202_f02atk', 1)
    physicsYImpulse(0)
    physicsXImpulse(80000)
    sprite('ny202_f02atk', 4)
    RefreshMultihit()
    loopRest()
    label(580)
    sprite('ny202_f02atk', 20)
    SetAcceleration(0)
    XImpulseAcceleration(-2)
    EndAttack()
    BlendMode_Normal()
    AlphaValue(120)
    ConstantAlphaModifier(-10)
    CreateParticle('nyef_cfanneldel', 0)


@State
def NY_SumDDMultiSword():

    def upon_IMMEDIATE():
        RunLoopUpon(17, 80)

        def upon_17():
            sendToLabel(1)
        AddX(100000)
        AddY(250000)

        def upon_41():
            Unknown2064(1)
            TriggerUponForState('NY_MultiSword', 41)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_SumMultiSwordBigmc', -1)
    label(0)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 8)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 9)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 10)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 11)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 12)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 13)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 14)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 15)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 16)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 17)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 18)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 19)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 20)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 21)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 22)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 23)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 24)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 25)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 26)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 27)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 28)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 29)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 30)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 31)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 32)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSword', 33)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 4)


@State
def NY_MultiSword():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(3)
        Damage(160)
        AttackP1(100)
        AttackP2(79)
        SingleProration(1)
        AirHitstunAnimation(12)
        AirPushbackX(80000)
        AirPushbackY(1000)
        YImpulseBeforeWallbounce(5)
        AirUntechableTime(40)
        WallbounceReboundTime(5)
        Hitstop(2)
        HitsparkSize(400)
        UseSlashHitspark(1)
        StarterRating(2)
        VoodooDamageMultiplier(2)
        if SLOT_IsUnlimited:
            Damage(140)
        PaletteIndex(2)
        AlphaValue(0)
        SetZVal(-50)
        ContinueState(120)

        def upon_OPPONENT_HIT_OR_BLOCK():
            sendToLabel(1)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageInterval(2)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        CollideWithWall(1)
        PrivateSE('nyse_00')

        def upon_45():
            if SLOT_StateDuration > 70:
                clearUponHandler(45)
                ObjectUpon(LANDING, 41)
        Unknown2064(0)

        def upon_41():
            Unknown2064(1)
            CHStateIfCHStart(2)
        CHStateIfCHStart(2)
    sprite('vrnyef_mltswd00', 1)
    CreateObject('NY_SumMultiSwordMc', -1)
    AddX(-80000)
    ConstantAlphaModifier(40)
    physicsXImpulse(29900)
    sprite('vrnyef_mltswd01', 1)
    sprite('vrnyef_mltswd02', 1)
    sprite('vrnyef_mltswd03', 1)
    sprite('vrnyef_mltswd04', 1)
    sprite('vrnyef_mltswd05', 1)
    XImpulseAcceleration(600)
    label(0)
    sprite('vrnyef_mltswdatk', 2)
    CreateParticle('nyef_sumDDmultikksn00', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrnyef_mltswdatk', 6)
    EndAttack()
    ConstantAlphaModifier(-30)
    EndMomentum(1)
    SetScaleXPerFrame(100)
    SetScaleSpeedY(-100)


@State
def NY_SumDDMultiSwordOD():

    def upon_IMMEDIATE():
        RunLoopUpon(17, 120)

        def upon_17():
            sendToLabel(1)
        AddX(100000)
        AddY(250000)

        def upon_41():
            Unknown2064(1)
            TriggerUponForState('NY_MultiSwordOD', 41)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_SumMultiSwordBigmcOD', -1)
    label(0)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 8)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 9)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 10)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 11)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 12)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 13)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 14)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 15)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 16)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 17)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 18)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 19)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 20)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 21)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 22)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 23)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 24)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 25)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 26)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 27)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 28)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 29)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 30)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 31)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 32)
    sprite('vrnyef_multiswddmy', 4)
    CreateObject('NY_MultiSwordOD', 33)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    sprite('null', 4)
    TriggerUponForState('NY_SumMultiSwordBigmcOD', 32)


@State
def NY_MultiSwordOD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(3)
        Damage(160)
        AttackP1(100)
        AttackP2(79)
        SingleProration(1)
        AirHitstunAnimation(12)
        AirPushbackX(80000)
        AirPushbackY(1000)
        YImpulseBeforeWallbounce(5)
        AirUntechableTime(40)
        WallbounceReboundTime(5)
        Hitstop(2)
        HitsparkSize(400)
        UseSlashHitspark(1)
        StarterRating(2)
        VoodooDamageMultiplier(2)
        AttackType(4)
        if SLOT_IsUnlimited:
            Damage(140)
        PaletteIndex(2)
        AlphaValue(0)
        SetZVal(-50)
        ContinueState(120)

        def upon_OPPONENT_HIT_OR_BLOCK():
            sendToLabel(1)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageInterval(2)
        AfterimageCount(2)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        CollideWithWall(1)
        PrivateSE('nyse_00')

        def upon_45():
            if SLOT_StateDuration > 70:
                clearUponHandler(45)
                ObjectUpon(LANDING, 41)
        Unknown2064(0)

        def upon_41():
            Unknown2064(1)
            CHStateIfCHStart(2)
        CHStateIfCHStart(2)
    sprite('vrnyef_mltswd00', 1)
    CreateObject('NY_SumMultiSwordMc', -1)
    AddX(-80000)
    ConstantAlphaModifier(40)
    physicsXImpulse(29900)
    sprite('vrnyef_mltswd01', 1)
    sprite('vrnyef_mltswd02', 1)
    sprite('vrnyef_mltswd03', 1)
    sprite('vrnyef_mltswd04', 1)
    sprite('vrnyef_mltswd05', 1)
    XImpulseAcceleration(600)
    label(0)
    sprite('vrnyef_mltswdatk', 2)
    CreateParticle('nyef_sumDDmultikksn00', -1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrnyef_mltswdatk', 6)
    EndAttack()
    ConstantAlphaModifier(-30)
    EndMomentum(1)
    SetScaleXPerFrame(100)
    SetScaleSpeedY(-100)


@State
def monoeye_line():

    def upon_IMMEDIATE():
        Visibility(1)
        CallObject('MonoeyeLine')
        E0EAEffectPolyline('vr_monoeye.hip', 2000)
    sprite('null', 32767)


@State
def EF_ny300():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        AddY(-30000)
    sprite('vrnyef300_parts1_00', 2)
    sprite('vrnyef300_parts1_01', 2)
    sprite('vrnyef300_parts1_02', 2)
    sprite('vrnyef300_parts1_03', 2)
    sprite('vrnyef300_parts1_04', 2)
    CreateObject('EF_ny300_parts2', 0)
    PrivateSE('nyse_31')
    sprite('vrnyef300_parts1_05', 2)
    sprite('vrnyef300_parts1_06', 2)
    sprite('vrnyef300_parts1_07', 1)
    sprite('vrnyef300_parts1_08', 1)
    sprite('vrnyef300_parts1_09', 1)
    sprite('vrnyef300_parts1_10', 1)
    sprite('vrnyef300_parts1_11', 1)
    sprite('vrnyef300_parts1_12', 35)
    sprite('vrnyef300_parts1_12', 12)
    ConstantAlphaModifier(-20)
    BlendMode_Normal()
    CreateObject('DIST_NY5D', 0)
    CreateParticle('nyef_cfanneldel', 0)


@State
def EF_ny300_parts2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Add()
        AbsoluteY(275000)
        XPositionRelativeFacing(120000)
    sprite('vrnyef300_parts2_00', 5)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrnyef300_parts2_00', 3)
    SetScaleSpeedY(0)
    CreateObject('EF_ny300_parts3', 0)
    sprite('vrnyef300_parts2_00', 36)
    sprite('vrnyef300_parts2_00', 12)
    ConstantAlphaModifier(-20)
    BlendMode_Normal()


@State
def EF_ny300_parts3():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Add()
        AbsoluteY(320000)
        XPositionRelativeFacing(95000)
    sprite('vrnyef300_parts3_00', 5)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrnyef300_parts3_00', 1)
    CreateObject('EF_ny300_parts4', 0)
    sprite('vrnyef300_parts3_00', 30)
    sprite('vrnyef300_parts3_00', 12)
    ConstantAlphaModifier(-20)
    BlendMode_Normal()


@State
def EF_ny300_parts4():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Add()
        AbsoluteY(248000)
        XPositionRelativeFacing(30000)
    sprite('vrnyef300_parts5_00', 5)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrnyef300_parts5_00', 1)
    CreateObject('EF_ny300_parts5', 0)
    sprite('vrnyef300_parts5_00', 26)
    sprite('vrnyef300_parts5_00', 12)
    ConstantAlphaModifier(-20)
    BlendMode_Normal()


@State
def EF_ny300_parts5():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(2)
        PaletteIndex(1)
        BlendMode_Add()
        AbsoluteY(300000)
        XPositionRelativeFacing(36000)
    sprite('vrnyef300_parts4_00', 4)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrnyef300_parts4_00', 22)
    sprite('vrnyef300_parts4_00', 12)
    PrivateSE('nyse_30')
    ConstantAlphaModifier(-20)
    BlendMode_Normal()


@State
def EntryFallSword():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        SetZVal(500)
        BlendMode_Normal()
        AbsoluteY(760000)
        AddX(-140000)
    sprite('vrnyef600_swd', 12)
    physicsYImpulse(-60000)
    sprite('vrnyef600_swd', 5)
    physicsYImpulse(-2000)
    CreateParticle('rmef_entrymc', 104)
    sprite('vrnyef600_swd', 5)
    physicsYImpulse(-1000)
    sprite('vrnyef600_swd', 10)
    physicsYImpulse(-500)
    sprite('vrnyef600_swd', 10)
    sprite('vrnyef600_swd', 12)
    CreateParticle('nyef_entrylightA', 0)
    CommonSE('022_magiccircle_a')
    sprite('vrnyef600_swd', 6)
    CreateParticle('nyef_entrylightB', 0)


@State
def EntryFallSword_RGVsNY():

    def upon_IMMEDIATE():
        SetZVal(500)
        BlendMode_Normal()
        AbsoluteY(760000)
        AddX(-140000)
    sprite('vrnyef600_swd', 12)
    physicsYImpulse(-60000)
    sprite('vrnyef600_swd', 5)
    physicsYImpulse(-2000)
    CreateParticle('rmef_entrymc', 104)
    sprite('vrnyef600_swd', 5)
    physicsYImpulse(-1000)
    sprite('vrnyef600_swd', 10)
    physicsYImpulse(-500)
    sprite('vrnyef600_swd', 10)
    EndMomentum(1)
    uponSendToLabel(32, 1)
    label(0)
    sprite('vrnyef600_swd', 1)
    gotoLabel(0)
    label(1)
    clearUponHandler(32)
    sprite('vrnyef600_swd', 12)
    CreateParticle('nyef_entrylightA', 0)
    CommonSE('022_magiccircle_a')
    sprite('vrnyef600_swd', 6)
    CreateParticle('nyef_entrylightB', 0)


@State
def RLAstSmoke():

    def upon_IMMEDIATE():
        LinkParticle('nyef_rlAHsmoke')
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
    sprite('null', 65)
    AlphaValue(0)
    ConstantAlphaModifier(3)
    sprite('null', 32767)
    ConstantAlphaModifier(0)


@State
def Changering():

    def upon_IMMEDIATE():
        Eff3DEffect('nyef_modechange00', '')
        LinkParticle('nyef_changering_jizoku')
        FaceSpawnLocation()
        PaletteIndex(1)
        ColorFromPaletteIndex(83)
        BlendMode_Normal()
        AlphaValue(0)
        Size(380)

        def upon_16():
            PrivateFunction3(3, 0, 200000, 50, 1)
        uponSendToLabel(32, 0)
    sprite('null', 10)
    ConstantAlphaModifier(26)
    sprite('null', 32767)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    CreateParticle('nyef_ringend_02', -1)
    clearUponHandler(32)
    ConstantAlphaModifier(-12)
    sprite('null', 1)
    ExitState()


@State
def ModeChangeEf():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        AlphaValue(255)
        CallPrivateEffect('nyef_changeeff_addtb')
        AddY(250000)
    sprite('null', 30)
    sprite('null', 30)
    ConstantAlphaModifier(-9)


@State
def __407slash():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        BlendMode_Normal()
        AlphaValue(150)
        Size(950)
        Eff3DEffect('nyef_407slash', '')
        AddY(120000)
    sprite('null', 28)


@State
def NY_BackShot():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(80)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(2)
        AirPushbackY(-80000)
        YImpulseBeforeWallbounce(0)
        GroundBounce(1)
        AirHitstunAfterWallbounce(44)
        BouncePercentage(40)
        UseSlashHitspark(1)
        StarterRating(2)
        Size(1000)
        PaletteIndex(1)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageCount(3)
        AfterimageSize_1(1000)
        AfterimageSize_2(1000)
        physicsXImpulse(10000)
        physicsYImpulse(-8000)
        RotationSomething(0)
        CancelIfPlayerHit(3)

        def upon_32():
            GroundedHitstunAnimation(2)

        def upon_EVERY_FRAME():
            if SLOT_YDistanceFromFloor <= 80000:
                sendToLabel(1)
        SameMoveProration(1)
    sprite('vrnyef_swdh00', 1)
    CreateObject('NY_SummonA', 0)
    CreateObject('NY_BackShotEffLoop', -1)
    sprite('vrnyef_swdh01', 1)
    sprite('vrnyef_swdh02', 1)
    sprite('vrnyef_swdh03', 1)
    sprite('vrnyef_swdh04', 1)
    XImpulseAcceleration(200)
    YAccel(200)
    sprite('vrnyef_swdh05', 1)
    XImpulseAcceleration(200)
    YAccel(200)
    sprite('vrnyef_swdhatk', 1)
    StartMultihit()
    XImpulseAcceleration(200)
    YAccel(200)
    sprite('vrnyef_swdhatk', 30)
    label(1)
    sprite('vrnyef_swddel', 6)
    clearUponHandler(EVERY_FRAME)
    StartMultihit()
    callSubroutine('DriveSwordLandingParam')


@State
def NY_BackShotEffLoop():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
    sprite('keep', 5)
    CreateObject('NY_BackShotEff', -1)
    label(0)
    sprite('keep', 4)
    CreateParticle('rmef_backshot', -1)
    gotoLabel(0)


@State
def NY_BackShotEff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        Eff3DEffect('rm_backshot00', '')
        BlendMode_Add()
        PaletteIndex(1)
        ColorFromPaletteIndex(241)
        AlphaValue(0)
        Size(650)
    sprite('null', 5)
    ConstantAlphaModifier(51)
    sprite('null', 14)
    SetScaleSpeed(10)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def RM_DDSlashEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('rm_440slasheff00', '')
        LinkParticle('rmef_440slash')
        AddY(250000)
        RotationAngle(45000)
        AddRotationPerFrame(-3000)
        Size(1300)
    sprite('null', 15)
    sprite('null', 10)
    AddRotationPerFrame(-24000)
    ConstantAlphaModifier(-26)


@State
def RM_DDSlashEffLast():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('rm_440slasheff00', '')
        LinkParticle('rmef_440slash')
        AddY(250000)
        RotationAngle(45000)
        AddRotationPerFrame(-3000)
        Size(1300)
    sprite('null', 7)
    sprite('null', 10)
    AddRotationPerFrame(-18000)
    ConstantAlphaModifier(-26)


@State
def RM_DDSlashEffEX():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('rm_440slasheff01', '')
        LinkParticle('rmef_440slash')
        AddY(250000)
        RotationAngle(45000)
        AddRotationPerFrame(-3000)
        Size(1600)
    sprite('null', 15)
    sprite('null', 10)
    AddRotationPerFrame(-24000)
    ConstantAlphaModifier(-26)


@State
def RM_DDSlashEffLastEX():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnorePauses(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('rm_440slasheff01', '')
        LinkParticle('rmef_440slash')
        AddY(250000)
        RotationAngle(45000)
        AddRotationPerFrame(-3000)
        Size(1800)
    sprite('null', 7)
    sprite('null', 5)
    AddRotationPerFrame(-18000)
    ConstantAlphaModifier(-51)


@State
def RM_StandEffLoop():

    def upon_IMMEDIATE():
        CancelIfPlayerHit(3)

        def upon_EVERY_FRAME():
            EffectPosition(3, 110)
        SLOT_7 = 1

        def upon_STATE_END():
            SLOT_7 = 0
    sprite('null', 7)
    CreateObject('RM_StandEff2', -1)
    CreateObject('RM_StandEff', -1)
    sprite('null', 7)
    CreateObject('RM_StandEff', -1)
    sprite('null', 7)
    CreateObject('RM_StandEff', -1)
    sprite('null', 7)
    CreateObject('RM_StandEff', -1)


@State
def RM_StandEff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        CancelIfPlayerHit(3)
        Eff3DEffect('nyef_standeff00', '')
        Size(1500)
        AddX(-20000)
        AlphaValue(80)
        RandAddRotation(0, 3600000)
        RandAddScaleX(-600, 500)
        DeviationX(-25000, 25000)
        DeviationY(-25000, 25000)
        BlendMode_Add()
        PaletteIndex(1)
        ColorFromPaletteIndex(241)

        def upon_53():
            Visibility(1)
    sprite('null', 21)
    CreateObject('RM_StandEffSub', -1)
    SetScaleSpeed(-3)
    CreateParticle('rm_standeff00', -1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def RM_StandEffSub():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        CancelIfPlayerHit(3)
        Eff3DEffect('nyef_standeff00_sub', '')
        LinkParticle('rm_standeffcore')
        PaletteIndex(1)
        ColorFromPaletteIndex(242)
        Size(1500)
        AlphaValue(80)
        RandAddScaleX(-600, 500)
        DeviationX(-25000, 25000)
        DeviationY(-25000, 25000)

        def upon_53():
            Visibility(1)
    sprite('null', 21)
    SetScaleSpeed(-3)
    CreateParticle('rm_standeff00', -1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def RM_StandEff2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        CancelIfPlayerHit(3)
        Eff3DEffect('nyef_standeff01', '')
        Size(1750)
        AddY(-20000)
        BlendMode_Add()
        PaletteIndex(1)
        ColorFromPaletteIndex(241)
        AlphaValue(0)

        def upon_53():
            Visibility(1)
    sprite('null', 10)
    ConstantAlphaModifier(7)
    sprite('null', 10)
    ConstantAlphaModifier(0)
    sprite('null', 10)
    ConstantAlphaModifier(-7)


@State
def RM_SummonEff3d():

    def upon_IMMEDIATE():
        Eff3DEffect('nyef_standeff01', '')
        FaceSpawnLocation()
        Size(1450)
        PaletteIndex(1)
        ColorFromPaletteIndex(243)
        BlendMode_Normal()
        AlphaValue(0)
        IgnoreScreenfreeze(1)

        def upon_53():
            Visibility(1)
    sprite('null', 5)
    ConstantAlphaModifier(30)
    sprite('null', 8)
    ConstantAlphaModifier(0)
    sprite('null', 5)
    ConstantAlphaModifier(-30)


@State
def NY_Sword4D_Event():

    def upon_IMMEDIATE():
        callSubroutine('DriveSwordInit')

        def upon_32():
            if SLOT_19 > 600000:
                TeleportToObject(22)
                AddX(100000)
            else:
                AddX(650000)
                AddX(100000)
            AbsoluteY(580000)
            CreateObject('NY_SummonA', 0)

        def upon_33():
            if SLOT_19 > 600000:
                TeleportToObject(22)
                AddX(-25000)
            else:
                AddX(625000)
            AbsoluteY(580000)
            CreateObject('NY_SummonA', 0)
        physicsXImpulse(-1666)
        physicsYImpulse(-4333)
        RotationSomething(0)
        PushbackX(-20000)
        HitOverhead(2)
    sprite('vrnyef_swdd00', 4)
    AttackOff()
    sprite('vrnyef_swdd01', 4)
    sprite('vrnyef_swdd02', 4)
    sprite('vrnyef_swdd03', 4)
    sprite('vrnyef_swdd04', 3)
    sprite('vrnyef_swdd05', 3)
    sprite('vrnyef_swddatk', 3)
    XImpulseAcceleration(1100)
    YAccel(1100)
    sprite('vrnyef_swddatk', 2)
    RefreshMultihit()
    label(1)
    sprite('vrnyef_swddel', 12)
    callSubroutine('DriveSwordLandingParam')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    callSubroutine('DriveSwordBreakParam')


@State
def Event_EF_ny300():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        PaletteIndex(1)
        AddY(-30000)

        def upon_32():
            TriggerUponForState('Event_EF_ny300_parts2', 32)
            TriggerUponForState('Event_EF_ny300_parts3', 32)
            TriggerUponForState('Event_EF_ny300_parts4', 32)
            TriggerUponForState('Event_EF_ny300_parts5', 32)
            sendToLabel(0)
    sprite('vrnyef300_parts1_00', 2)
    sprite('vrnyef300_parts1_01', 2)
    sprite('vrnyef300_parts1_02', 2)
    sprite('vrnyef300_parts1_03', 2)
    sprite('vrnyef300_parts1_04', 2)
    CreateObject('Event_EF_ny300_parts2', 0)
    PrivateSE('nyse_31')
    sprite('vrnyef300_parts1_05', 2)
    sprite('vrnyef300_parts1_06', 2)
    sprite('vrnyef300_parts1_07', 1)
    sprite('vrnyef300_parts1_08', 1)
    sprite('vrnyef300_parts1_09', 1)
    sprite('vrnyef300_parts1_10', 1)
    sprite('vrnyef300_parts1_11', 1)
    sprite('vrnyef300_parts1_12', 32767)
    loopRest()
    label(0)
    sprite('vrnyef300_parts1_12', 12)
    ConstantAlphaModifier(-20)
    BlendMode_Normal()
    CreateObject('DIST_NY5D', 0)
    CreateParticle('nyef_cfanneldel', 0)


@State
def Event_EF_ny300_parts2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        PaletteIndex(1)
        BlendMode_Add()
        AbsoluteY(275000)
        XPositionRelativeFacing(120000)

        def upon_32():
            sendToLabel(0)
    sprite('vrnyef300_parts2_00', 5)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrnyef300_parts2_00', 3)
    SetScaleSpeedY(0)
    CreateObject('Event_EF_ny300_parts3', 0)
    sprite('vrnyef300_parts2_00', 32767)
    loopRest()
    label(0)
    sprite('vrnyef300_parts2_00', 12)
    ConstantAlphaModifier(-20)
    BlendMode_Normal()


@State
def Event_EF_ny300_parts3():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        PaletteIndex(1)
        BlendMode_Add()
        AbsoluteY(320000)
        XPositionRelativeFacing(95000)

        def upon_32():
            sendToLabel(0)
    sprite('vrnyef300_parts3_00', 5)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrnyef300_parts3_00', 1)
    CreateObject('Event_EF_ny300_parts4', 0)
    sprite('vrnyef300_parts3_00', 32767)
    loopRest()
    label(0)
    sprite('vrnyef300_parts3_00', 12)
    ConstantAlphaModifier(-20)
    BlendMode_Normal()


@State
def Event_EF_ny300_parts4():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        PaletteIndex(1)
        BlendMode_Add()
        AbsoluteY(248000)
        XPositionRelativeFacing(30000)

        def upon_32():
            sendToLabel(0)
    sprite('vrnyef300_parts5_00', 5)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrnyef300_parts5_00', 1)
    CreateObject('Event_EF_ny300_parts5', 0)
    sprite('vrnyef300_parts5_00', 32767)
    loopRest()
    label(0)
    sprite('vrnyef300_parts5_00', 12)
    ConstantAlphaModifier(-20)
    BlendMode_Normal()


@State
def Event_EF_ny300_parts5():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        PaletteIndex(1)
        BlendMode_Add()
        AbsoluteY(300000)
        XPositionRelativeFacing(36000)

        def upon_32():
            sendToLabel(0)
    sprite('vrnyef300_parts4_00', 4)
    AlphaValue(0)
    ConstantAlphaModifier(50)
    sprite('vrnyef300_parts4_00', 32767)
    loopRest()
    label(0)
    sprite('vrnyef300_parts4_00', 12)
    PrivateSE('nyse_30')
    ConstantAlphaModifier(-20)
    BlendMode_Normal()


@State
def ActEvent_rmvsrl_DD():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        PaletteIndex(1)
        AddX(440000)
        AddY(640000)
        SetZVal(-1)
        AlphaValue(0)
        WallCollisionDetection(1)
        EnableAfterimage(1)
        AfterimageBlendMode(2)
        AfterimageInterval(1)
        AfterimageCount(3)
        AfterimageColor_1(0, 255, 0, 0)
        AfterimageColor_2(255, 0, 0, 0)
        AfterimageSize_1(1030)
        AfterimageSize_2(1040)
    sprite('vrnyef_ddbigswd00', 41)
    CreateObject('NY_SumBigSword', -1)
    CreateObject('SummonDDBigSwordSub', -1)
    ConstantAlphaModifier(10)
    AddY(512000)
    physicsYImpulse(-1000)
    CreateParticle('nyef_bottomswd', -1)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_ddbigswd01', 1)
    AddY(-200000)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    ScreenShake(0, 30000)
    PrivateSE('nyse_04')
    sprite('vrnyef_ddbigswd02', 1)
    AddY(-150000)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_ddbigswd03', 1)
    AddY(-50000)
    CreateParticle('rmef_sumDDshock', 104)
    CreateParticle('nyef_sumDDshocklight00', 0)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
    sprite('vrnyef_ddbigswd04', 8)
    AlphaValue(255)
    SetScaleSpeed(1)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    sprite('vrnyef_ddbigswd05', 25)
    physicsYImpulse(2000)
    ConstantAlphaModifier(-10)
    CreateParticle('nyef_bottomswd', 0)
    CreateParticle('nyef_bottomswd', 1)
    CreateParticle('nyef_bottomswd', 2)
    CreateParticle('nyef_bottomswd', 3)
    CreateParticle('nyef_bottomswd', 4)
    CreateParticle('nyef_bottomswd', 5)
